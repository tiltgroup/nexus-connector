---
name: create-load
description: Create a new load (shipment) in Nexus from details the user gives — customer, pickup and delivery stops, appointments, equipment, commodity, weight and rates — or from a pasted rate confirmation or order email. Use when the user wants to enter, book or build a load.
---

# Create a load

Creating a load writes real data. Follow these steps in order.

## 1. Gather the details

At minimum you need:

- the customer;
- the pickup and delivery stops, with addresses and appointment dates and times;
- the equipment type;
- what is moving: commodity, weight and pieces.

Optional details include the customer rate, carrier pay, references (PO, BOL, pickup number), freight requirements, temperature control and instructions. Compare with what the input type requires, and ask only for what is missing; don't interrogate the user about optional fields.

## 2. Resolve the related records

Look up the ids of existing records instead of guessing them: the customer, the equipment type, the mode, and the reference types if references are given. When a name matches more than one record, ask which one. Never create a customer or carrier as a side effect.

## 3. Check before creating

If the schema offers a validation or dry-run mutation for loads, run it first with the same input; it saves nothing and returns the errors to fix.

## 4. Confirm, then create

Show the user a short summary of the load exactly as it will be created: customer, each stop with its appointment, equipment, commodity and weight, rates, and references. Wait for an explicit yes. Only then create the load and reply with its id and status.

If creation fails, report the error in plain words and what needs to change; don't retry with guessed values.
