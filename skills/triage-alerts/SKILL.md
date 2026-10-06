---
name: triage-alerts
description: Review and triage open shipment alerts and exceptions in Nexus — delays, lost tracking signal, off-route trucks, missing documents, detention, claims and similar. Use when the user asks what needs attention, which loads have problems, or wants to acknowledge, snooze or resolve alerts.
---

# Triage exceptions and alerts

## 1. Pull the open alerts

`nexus_query` with `shipmentAlerts(...)`:

- Open alerts only: `where: { column: IS_RESOLVED, operator: EQ, value: false }`.
- Narrow with the `ShipmentAlertFilters` columns (`TYPE`, `SEVERITY`, `CREATED_AT`), `teamIds`, or `shipmentId` for a single load. Pass `snoozed: false` to hide alerts the user already snoozed.
- Select `id`, `type`, `severity`, `note`, `createdAt`, `acknowledgedAt`, `resolveAt`, and the load: `shipment { id status itracker_reference_id }`.

Severity runs `CRITICAL` > `MAJOR` > `MINOR` > `LOW`. Confirm the enum values and fields with `nexus_describe_types` (`ShipmentAlert`, `ShipmentAlertType`) before filtering.

## 2. Triage

- Group the alerts by severity, then by load, so one problem load reads as one item.
- For tracking-related types (lost signal, off route, stopped, pickup or delivery delay), check the live picture with the track-load workflow before recommending action.
- For each item give: what happened, how long it has been open, the likely next step (call the carrier, update the customer, request documents) and who would normally own it.
- Keep the summary short: the user wants a work queue, not a report.

## 3. Act on alerts (changes data)

The mutations are `acknowledgeShipmentAlert(ids)`, `snoozeShipmentAlerts(ids)`, `unsnoozeShipmentAlerts(ids)`, `resolveShipmentAlert(id, resolutionNote)`, `resolveShipmentAlerts(ids, resolutionNote)` and `createShipmentAlert(input)`.

Acknowledging and snoozing affect only the current user. Resolving notifies the load's watchers.

Before any `nexus_mutate` call, list exactly which alerts will change and how, and wait for the user's explicit confirmation. Never resolve an alert on your own judgement.

Link every load you mention to Nexus: `https://nexus.tiltgroup.com/shipments/<id>`.
