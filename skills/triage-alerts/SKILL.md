---
name: triage-alerts
description: Review and triage open shipment alerts and exceptions in Nexus — delays, lost tracking signal, off-route trucks, missing documents, detention, claims and similar. Use when the user asks what needs attention, which loads have problems, or wants to acknowledge, snooze or resolve alerts.
---

# Triage exceptions and alerts

## 1. Pull the open alerts

- Only unresolved alerts, and leave out ones the user has snoozed unless they ask for them.
- Narrow by severity, type, team or a single load when the user asks.
- For each alert, get its type, severity, note, when it was raised, whether it was acknowledged, and the load it belongs to.

## 2. Triage

- Group the alerts by severity, highest first, then by load, so one problem load reads as one item.
- For tracking-related alerts (lost signal, off route, stopped, pickup or delivery delay), check the live picture with the track-load skill before recommending action.
- For each item give: what happened, how long it has been open, the likely next step (call the carrier, update the customer, request documents) and who would normally own it.
- Keep the summary short: the user wants a work queue, not a report.

## 3. Act on alerts (changes data)

Search the schema for the alert mutations to acknowledge, snooze or resolve alerts. Read their descriptions: some actions affect only the current user, while resolving notifies the people watching the load.

Before any `nexus_mutate` call, list exactly which alerts will change and how, and wait for the user's explicit confirmation. Never resolve an alert on your own judgement.
