# Nexus connector for AI assistants

Connect your AI assistant to **Nexus**, the freight brokerage TMS, and **iTracker** live tracking. Ask about your loads in plain language and let the assistant help with the routine work:

- **Find loads:** list loads by status, customer, carrier, lane, dates, open alerts or coverage, with a link to each one in Nexus.
- **Track a load:** find a load by number, reference, customer or lane, and get its live position, ETA and delays from iTracker.
- **Triage alerts:** see which loads need attention, grouped by severity, and acknowledge, snooze or resolve alerts.
- **Create a load:** turn order details or a pasted rate confirmation into a validated Nexus load.
- **Quote and book:** request LTL quotes, compare carriers on price and transit time, and book the one you choose. You can also check lane pricing and historical rates for truckload.

## Choose your assistant

| Assistant | Status | Who sets it up | Guide |
|---|---|---|---|
| Claude (web, desktop, Claude Code) | Pilot | You, or your Claude organization owner | [Claude](docs/claude.md) |
| ChatGPT (Business, Enterprise) | Coming soon | Your ChatGPT workspace admin | [ChatGPT](docs/chatgpt.md) |
| Gemini Enterprise | Planned | Your Gemini Enterprise admin | [Gemini](docs/gemini.md) |

Every assistant connects to the same Nexus connector, a remote MCP server at `https://nexus.tiltgroup.com/api/mcp`, and uses the same workflows from [`skills/`](skills).

## Before you start

- You need a Nexus user account.
- An administrator in your company with the **Manage Integrations** permission must enable the AI connector in Nexus under **Settings → Integrations**. Until then, the connector refuses requests.
- The assistant acts **as you**. Every request runs with your own Nexus permissions, so it can see and change only what you could in Nexus yourself. You sign in on the Nexus login page; the assistant never sees your password.
- iTracker data is read-only through the connector.
- The assistant describes every change and asks for your confirmation before it creates, updates, books or resolves anything.

You can review or revoke the assistants connected to your account at any time in Nexus under **Settings → Integrations**.

## Example prompts

- "Where is load 48213 and will it make the delivery appointment?"
- "Which of my loads have critical alerts right now?"
- "Show me everything picking up in Texas tomorrow that still has no carrier."
- "Create a load for Acme Foods: pickup Dallas TX tomorrow 8am, deliver Atlanta GA Friday, 53' dry van, 38,000 lb of canned goods, customer rate $2,450."
- "Get LTL quotes for 4 pallets, class 70, 1,800 lb, from Chicago 60607 to Denver 80216, and book the cheapest one that arrives by Thursday."

## What's in this repository

| Path | What it is |
|---|---|
| `skills/` | The workflows, one `SKILL.md` per workflow. The single source for every assistant. |
| `.claude-plugin/`, `.mcp.json` | The Claude plugin and plugin marketplace. |
| `docs/` | Setup guides per assistant. |
| `scripts/package.sh` | Builds the downloads: one zip per skill for ChatGPT, and one instructions file for Gemini. |

Each [release](https://github.com/tiltgroup/nexus-connector/releases) has those downloads attached, so nobody has to build anything.

## Privacy and support

- Privacy policy: TODO_PRIVACY_POLICY_URL
- Support: TODO_SUPPORT_CONTACT

Data you access through the connector stays subject to your company's agreement with Tilt Group. What you send to your AI assistant is handled under your agreement with its provider.

## License

TODO_LICENSE
