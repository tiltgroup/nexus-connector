# Nexus in ChatGPT

> **Coming soon.** ChatGPT support is not available yet. This page describes how setup will work.

Needs a ChatGPT **Business or Enterprise** workspace. ChatGPT only lets workspace admins add custom connectors, so Free, Plus and Pro accounts can't use it. Two pieces: the **app** gives ChatGPT access to Nexus, and the **skills** teach it the Nexus workflows.

## Workspace admin, once

1. **Get the sign-in credentials.** Ask Tilt Group support for the ChatGPT client ID and client secret for your company. They identify ChatGPT to the Nexus login page; keep the secret private.
2. **Allow custom apps:** in workspace settings, turn on developer mode (custom MCP connectors) for yourself.
3. **Create the app:** add a new custom app with the connector URL `https://nexus.tiltgroup.com/api/mcp`, choose OAuth, and enter the client ID and secret from step 1. Leave the registration URL empty.
4. **Publish it** to the workspace, or to the groups that work with loads.
5. **Add the skills:** download the four skill zips from the latest [release](https://github.com/tiltgroup/nexus-connector/releases). For each one: **Skills → Create → Upload from your computer**, pick the zip, then share the skill with the same people.

## Everyone else

Open the Nexus app in ChatGPT, select **Connect**, and sign in with your Nexus account. The skills are used automatically when a request matches, or you can mention one by name.
