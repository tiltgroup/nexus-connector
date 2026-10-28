# Nexus in Claude

Works in Claude on the web, the desktop app, Cowork and Claude Code. Two pieces: the **connector** gives Claude access to Nexus, and the **plugin** teaches it the Nexus workflows.

## Team and Enterprise plans (recommended)

An owner sets it up once for everyone.

1. **Add the connector:** **Organization settings → Connectors → Add → Custom → Web**. Name: `Nexus`. URL: `https://nexus.tiltgroup.com/api/mcp`.
2. **Add the plugin:** **Organization settings → Plugins & skills**. Add this repository (`tiltgroup/nexus-connector`) to your organization's plugin marketplace, then make the `nexus` plugin available to the people who work with loads. Turn on auto-install so it appears for them without any steps.

Each person then opens **Settings → Connectors**, selects **Connect** next to Nexus, and signs in with their Nexus account. That's all.

## Pro and Max plans

1. **Settings → Connectors → Add custom connector**. Name: `Nexus`. URL: `https://nexus.tiltgroup.com/api/mcp`.
2. Select **Connect** and sign in with your Nexus account.
3. Optional but recommended: install the plugin so Claude knows the workflows. Add `tiltgroup/nexus-connector` as a plugin marketplace and install the `nexus` plugin.

## Claude Code

```bash
claude plugin marketplace add tiltgroup/nexus-connector
claude plugin install nexus@nexus-connector
```

The plugin registers the Nexus connector. The first time Claude uses it, run `/mcp` and sign in with your Nexus account.

## Testing against another environment

The plugin connects to production unless `NEXUS_MCP_URL` is set, so testers can point it at another Nexus environment:

| Environment | `NEXUS_MCP_URL` |
|---|---|
| Development | `https://nexus.dev.tltgrp.com/api/mcp` |
| Staging | `https://nexus.staging.tltgrp.com/api/mcp` |

The broker you sign in with must have the connection turned on in that environment's Nexus, under **Workspace settings → Connections → MCP** (**Allow MCP connection**).

**Claude Code:** start Claude with the variable set, for example `NEXUS_MCP_URL=https://nexus.dev.tltgrp.com/api/mcp claude`, then run `/mcp` and sign in.

**Claude on the web, desktop app and Cowork:** these ignore `NEXUS_MCP_URL`, so add the environment as its own connector:
1. **Add custom connector**, with the URL from the table above.
2. Under the OAuth options, choose **Use your own OAuth client** and enter client ID `ai-claude` and that environment's client secret (Secret Manager: `ai-claude-client-secret`).
3. **Connect** and sign in with your account for that environment.
