#!/usr/bin/env python3
"""Build and inspect a public-review draft, preserving the ordinary package.
Requires PyYAML and Pillow. This is local structural validation, not Portal approval.
"""
import copy
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile
import zipfile

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def merge(base, overlay):
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            merge(base[key], value)
        else:
            base[key] = copy.deepcopy(value)


def validate(archive):
    with zipfile.ZipFile(archive) as z:
        require(z.testzip() is None, 'Corrupt ZIP member')
        names = z.namelist()
        require(len(names) == len(set(names)), 'Duplicate ZIP paths')
        for entry in z.infolist():
            path = PurePosixPath(entry.filename)
            require(not path.is_absolute() and '..' not in path.parts, 'Unsafe archive path')
            require(not stat.S_ISLNK(entry.external_attr >> 16), 'Symlink in archive')
            require(not any(p.startswith('.') for p in path.parts), 'Hidden file in upload')
        manifest = json.loads(z.read('plugin.json'))
        require(manifest['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'Manifest schema')
        require(re.fullmatch(r'(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?', manifest['name']) and len(manifest['name']) <= 64, 'Plugin name')
        require(re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']), 'Version')
        ext = manifest['extensions']['com.openai']
        require(manifest.get('apps') is None and ext.get('apps') is None, 'Private app binding')
        interface = ext['interface']
        for field, limit in [('displayName', 30), ('shortDescription', 30), ('longDescription', 4000), ('developerName', 80)]:
            require(isinstance(interface[field], str) and 0 < len(interface[field].strip()) <= limit, field)
        require(interface['category'] in {'Business & Operations','Communication','Creativity','Data & Analytics','Developer Tools','Education & Research','Entertainment','Finance','Healthcare','Other','Productivity','Scientific Research','Security','Travel'}, 'Category')
        prompts = interface['defaultPrompt']
        if isinstance(prompts, str):
            prompts = [prompts]
        require(len(prompts) <= 3 and all(isinstance(p, str) and p.strip() and len(p) <= 128 and '\n' not in p and '@' not in p for p in prompts), 'Default prompts')
        require(len(set(' '.join(p.split()) for p in prompts)) == len(prompts), 'Duplicate prompts')
        for field, minimum in [('logo',256), ('composerIcon',48)]:
            path = PurePosixPath(interface[field])
            require(not path.is_absolute() and '..' not in path.parts, 'Unsafe icon path')
            blob = z.read(str(path))
            with Image.open(io.BytesIO(blob)) as im:
                require(im.format == 'PNG' and im.width == im.height and minimum <= im.width <= 4096 and len(blob) <= 5 * 1024 * 1024, field)
                im.verify()
        skills = [n for n in names if re.fullmatch(r'skills/[^/]+/SKILL.md', n)]
        require(len(skills) == 6, 'Expected six skills')
        seen = set()
        for name in skills:
            blob = z.read(name)
            require(len(blob) <= 1024 * 1024, 'Skill too large')
            parts = blob.decode('utf-8').split('---', 2)
            require(len(parts) == 3 and parts[0] == '', 'Missing skill frontmatter')
            meta = yaml.safe_load(parts[1])
            require(meta['name'] == PurePosixPath(name).parts[1] and meta['name'] not in seen, 'Skill name')
            require(isinstance(meta['description'], str) and meta['description'].strip() and parts[2].strip(), 'Skill description/body')
            seen.add(meta['name'])
        mcp = json.loads(z.read('mcp.json'))
        require(mcp['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json', 'MCP schema')
        require(len(mcp['mcpServers']) == 1, 'Review cases require exactly one MCP server')
        nexus = mcp['mcpServers']['nexus']
        require(nexus['type'] == 'streamable-http' and nexus['url'] == 'https://nexus.tiltgroup.com/api/mcp', 'MCP endpoint/transport')
        cases = ext['review']['test_cases']
        for kind, count in [('positive',5), ('negative',3)]:
            require(len(cases[kind]) == count, f'{kind} case count')
            for case in cases[kind]:
                fields = ['description', 'prompt'] + (['tools_triggered','expected_behavior'] if kind == 'positive' else [])
                require(all(isinstance(case.get(f), str) and case[f].strip() for f in fields), 'Case fields')
        require(ext['publication']['countries'] == [], 'Expected all-country targeting')
        print(f'PASS: ZIP integrity, {len(names)} files, six skills, icons, listing lengths, one MCP server, five positive and three negative case definitions.')
        for field in ['websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL']:
            if not interface.get(field):
                print(f'INCOMPLETE: {field}')
        if not ext['review'].get('demo_recording_url'):
            print('INCOMPLETE: demo_recording_url')
        print('DRAFT ONLY: URL content, policy coverage, review execution, tool annotations and Portal checks still need verification.')


def main():
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    merge(manifest['extensions']['com.openai'], json.loads((ROOT / 'submission/openai.json').read_text()))
    output = ROOT / 'dist/nexus-tms-openai-submission-draft.zip'
    output.parent.mkdir(exist_ok=True)
    # Build separately and replace only after the resulting archive passes checks.
    with tempfile.TemporaryDirectory() as temp:
        archive = Path(temp) / output.name
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('plugin.json', json.dumps(manifest, indent=2) + '\n')
            sources = [ROOT / 'mcp.json', ROOT / 'LICENSE']
            for directory in ['skills', 'assets']:
                sources.extend(sorted((ROOT / directory).rglob('*')))
            for path in sources:
                relative = path.relative_to(ROOT)
                require(not path.is_symlink(), f'Symlink: {relative}')
                if path.is_file() and not any(p.startswith('.') for p in relative.parts):
                    z.write(path, relative.as_posix())
        validate(archive)
        output.write_bytes(archive.read_bytes())
    print(output)


if __name__ == '__main__':
    main()
