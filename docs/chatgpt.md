# Nexus in ChatGPT

> **Pilot.** The connection works on paid ChatGPT plans. Installing the plugin from this repository is still being tested.

Two pieces: the **app** gives ChatGPT access to Nexus, and the **skills** teach it the Nexus workflows. The **Nexus TMS plugin** bundles both, with the Nexus logo.

To sign in, ChatGPT needs the Nexus client ID and client secret for ChatGPT. Ask Tilt Group support for them and keep the secret private.

## Add the app (tested)

Works on Plus, Pro, Business and Enterprise. On Business and Enterprise, a workspace admin may need to allow developer mode first.

1. On chatgpt.com, open **Settings → Apps → Advanced settings** and turn on **Developer mode**.
2. Back in **Settings → Apps**, select **Create** and enter:
   - Name: `Nexus TMS`
   - MCP server URL: `https://nexus.tiltgroup.com/api/mcp`
   - Authentication: **OAuth**, with the client ID and client secret from Tilt Group support
3. Select **Connect** and sign in with your Nexus account.

Workspace admins can then publish the app to the people who work with loads.

Write actions, such as creating a load, may need a Business or Enterprise plan; on Plus and Pro, ChatGPT may only read.

## Add the skills

Either download `nexus-tms-chatgpt.zip` from the latest [release](https://github.com/tiltgroup/nexus-connector/releases) and upload it as a plugin, or upload the single skill zips from the same release under **Skills → Create → Upload from your computer**.

In the ChatGPT desktop app you can also add this repository as a plugin marketplace (**Plugins → Add → Add a marketplace**, `tiltgroup/nexus-connector`) and install **Nexus TMS** from it. Updates arrive when the marketplace is refreshed.

## Using it

Pick **Nexus TMS** from the tools menu in a chat, or just ask about your loads. ChatGPT describes every change and asks for your confirmation before it creates, updates, books or resolves anything.

The broker you sign in with must have **Allow MCP connection** turned on in Nexus, under **Workspace settings → Connections → MCP**.
