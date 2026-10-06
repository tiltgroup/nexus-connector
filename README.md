# Nexus for Claude

Connect Claude to **Nexus**, the freight brokerage TMS, and **iTracker** live tracking. Ask Claude about your loads in plain language, and let it help with the routine work:

- **Track a load:** find a load by number, reference, customer or lane, and get its live position, ETA and delays from iTracker.
- **Triage alerts:** see which loads need attention, grouped by severity, and acknowledge, snooze or resolve alerts.
- **Create a load:** turn order details or a pasted rate confirmation into a validated Nexus load.
- **Quote and book:** request LTL quotes, compare carriers on price and transit time, and book the one you choose. You can also check lane pricing and historical rates for truckload.

This repository contains two parts:

1. **The Nexus connector:** a remote MCP server at `https://nexus.tiltgroup.com/api/mcp`. It gives Claude the tools to read Nexus and iTracker and to make changes in Nexus.
2. **The Nexus plugin:** skills that teach Claude the workflows above, plus the connector configuration for Claude Code.

## Before you start

- You need a Nexus user account.
- An administrator in your company with the **Manage Integrations** permission must enable the AI connector in Nexus under **Settings → Integrations**. Until then, the connector refuses requests.
- Claude acts **as you**. Every request runs with your own Nexus permissions, so Claude can see and change only what you could in Nexus yourself. Signing in happens on the Nexus login page; Claude never sees your password.
- iTracker data is read-only through the connector.
- Claude always describes a change and asks for your confirmation before it creates, updates, books or resolves anything.

You can review or revoke the apps connected to your account at any time in Nexus under **Settings → Integrations**.

## Set up in Claude (web and desktop)

1. Go to **Settings → Connectors** and choose **Add custom connector**.
2. Name: `Nexus`. URL: `https://nexus.tiltgroup.com/api/mcp`.
3. Select **Connect** and sign in with your Nexus account.
4. Optional but recommended: install the plugin from this repository so Claude knows the workflows. Add this repository as a plugin marketplace, then install the `nexus` plugin.

On a Team or Enterprise plan, an owner may need to add the connector for the organization first.

## Set up in Claude Code

```bash
claude plugin marketplace add tiltgroup/nexus-connector
claude plugin install nexus@nexus-connector
```

The plugin registers the Nexus connector. The first time Claude uses it, run `/mcp` and sign in with your Nexus account.

## Example prompts

- "Where is load 48213 and will it make the delivery appointment?"
- "Which of my loads have critical alerts right now?"
- "Create a load for Acme Foods: pickup Dallas TX tomorrow 8am, deliver Atlanta GA Friday, 53' dry van, 38,000 lb of canned goods, customer rate $2,450."
- "Get LTL quotes for 4 pallets, class 70, 1,800 lb, from Chicago 60607 to Denver 80216, and book the cheapest one that arrives by Thursday."

## Privacy and support

- Privacy policy: TODO_PRIVACY_POLICY_URL
- Support: TODO_SUPPORT_CONTACT

Data you access through the connector stays subject to your company's agreement with Tilt Group. What you send to Claude is handled under your agreement with Anthropic.

## License

TODO_LICENSE
