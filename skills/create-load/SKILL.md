---
name: create-load
description: Create a new load (shipment) in Nexus from details the user gives — customer, pickup and delivery stops, appointments, equipment, commodity, weight and rates — or from a pasted rate confirmation or order email. Use when the user wants to enter, book or build a load.
---

# Create a load

Creating a load writes real data. Follow these steps in order.

## 1. Gather the details

At minimum you need:

- the customer (client);
- the pickup and delivery stops, with addresses and appointment dates and times;
- the equipment type;
- what is moving: commodity, weight and pieces.

Optional details include customer rate (`client_payment`), carrier pay (`carrier_payout`), references (PO, BOL, pickup number), freight requirements, temperature control and instructions. Ask only for what is missing; don't interrogate the user about optional fields.

## 2. Resolve the related records

Look up ids instead of guessing them:

- the client: `clients` filtered by name;
- the equipment type and freight transportation mode;
- the reference types, if references are given.

When a name matches more than one record, ask which one. Never create a client or carrier as a side effect.

## 3. Build and check the input

- `nexus_describe_types` for `LoadInput`, `StopHasMany` and the `…BelongsTo` input types before writing the mutation. Relations are nested inputs, for example `client: { connect: <id> }`.
- Dry-run with `validateLoad(input: …)` through `nexus_mutate`. It saves nothing and returns validation errors to fix first.

## 4. Confirm, then create

Show the user a short summary of the load exactly as it will be created: customer, each stop with its appointment, equipment, commodity and weight, rates, and references. Wait for an explicit yes. Only then call `createLoad(input: …)` and reply with the new load id and status.

If creation fails, report the error in plain words and what needs to change; do not retry with guessed values.
