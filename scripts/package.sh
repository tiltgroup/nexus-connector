#!/usr/bin/env bash
# Builds the per-AI downloads from skills/, the single source of the workflows:
#   dist/skills/<name>.zip      one skill per zip, SKILL.md at the root (ChatGPT upload)
#   dist/nexus-instructions.md  every skill as one instructions text (Gemini agent)
#   dist/nexus-tms-chatgpt.zip  the ChatGPT plugin package (plugin.json, mcp.json, skills/, assets/)
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
dist="$root/dist"

# Claude and ChatGPT read different manifests; a release must not ship them out of step.
versions="$(python3 -c 'import json,sys; print(*(json.load(open(f))["version"] for f in sys.argv[1:]))' \
  "$root/plugin.json" "$root/.claude-plugin/plugin.json")"
read -r chatgpt_version claude_version <<< "$versions"
if [ "$chatgpt_version" != "$claude_version" ]; then
  echo "plugin.json is $chatgpt_version but .claude-plugin/plugin.json is $claude_version" >&2
  exit 1
fi

rm -rf "$dist"
mkdir -p "$dist/skills"

instructions="$dist/nexus-instructions.md"
cat > "$instructions" <<'EOF'
# Nexus workflows

You are connected to Nexus, a freight brokerage TMS, and iTracker live tracking through the Nexus connector. Every call runs as the signed-in user with that user's permissions. iTracker is read-only. Before any change in Nexus, state exactly what will change and wait for the user's explicit confirmation.

EOF

for dir in "$root"/skills/*/; do
  name="$(basename "$dir")"
  (cd "$dir" && zip -qr "$dist/skills/$name.zip" .)

  # Drop the YAML frontmatter; the body is the instructions.
  awk 'BEGIN { fm = 0 } NR == 1 && /^---$/ { fm = 1; next } fm && /^---$/ { fm = 0; next } !fm' "$dir/SKILL.md" >> "$instructions"
  printf '\n' >> "$instructions"
done

(cd "$root" && zip -qr "$dist/nexus-tms-chatgpt.zip" plugin.json mcp.json skills assets LICENSE)

echo "Built $(ls "$dist/skills" | wc -l | tr -d ' ') skill zips, $(basename "$instructions") and nexus-tms-chatgpt.zip in $dist"
