# Nexus in Gemini

> **Planned.** Gemini support is not available yet. This page describes how setup will work.

Needs **Gemini Enterprise**. Google offers custom MCP connections in Gemini Enterprise as a preview, and only admins can add them. The consumer Gemini app allows custom connectors only on personal Google accounts, so it doesn't work with company accounts.

## Gemini Enterprise admin, once

1. **Get the sign-in details.** Ask Tilt Group support for the Gemini OAuth details for your company: client ID, client secret, authorization URL, token URL and scopes. Keep the secret private.
2. **Add the connection:** add a custom MCP server connection with the URL `https://nexus.tiltgroup.com/api/mcp`, choose OAuth 2.0, and enter the details from step 1.
3. **Add the workflows:** download `nexus-instructions.md` from the latest [release](https://github.com/tiltgroup/nexus-connector/releases), and paste its contents as the instructions of the agent that uses the Nexus connection.
4. Make the agent available to the people who work with loads.

## Everyone else

Open the Nexus agent in Gemini Enterprise and sign in with your Nexus account when asked.
