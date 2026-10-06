---
name: track-load
description: Find a Nexus load (shipment) and report where it is right now using iTracker live tracking. Use when the user asks about a load's status, location, ETA, delay, driver, stops, or tracking history, by load number, reference, customer, carrier or lane.
---

# Find and track a load

Nexus holds the load; iTracker holds its live tracking. Every call runs as the signed-in user, so only loads that user can see are returned.

## 1. Find the load in Nexus

- With a Nexus load number, read that load directly.
- With anything else (a PO, BOL, PRO or other reference, a customer, carrier, lane or status), search the loads as in the find-loads skill.
- If several loads match, list them briefly (id, status, origin → destination, pickup date) and ask which one.
- Select what the answer needs: status, customer and carrier, the stops with their appointment and arrival times, and the load's iTracker reference (search the Nexus schema for `itracker`).

## 2. Get live tracking from iTracker

- The iTracker reference on the Nexus load identifies the same load in iTracker. If it is empty, the load isn't tracked in iTracker; say so and answer from Nexus data only.
- Search the iTracker schema for the load tracker and read it by that reference: its status, ETA, delay, stops, drivers and alerts.
- For the movement trail or the tracking timeline, search the iTracker schema for checkpoints and events.

## 3. Answer

Lead with the answer: where the load is, whether it is on time, and the ETA to the next stop, with times in the stop's local timezone. Then add the supporting detail: the last position and when it was recorded, the delay reason, and any open alerts. Say clearly when tracking data is stale or missing rather than guessing.

iTracker is read-only here. To change anything on a load, use the Nexus tools and follow the confirmation rule in the create-load skill.
