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
