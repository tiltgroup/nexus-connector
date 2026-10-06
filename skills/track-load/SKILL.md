---
name: track-load
description: Find a Nexus load (shipment) and report where it is right now using iTracker live tracking. Use when the user asks about a load's status, location, ETA, delay, driver, stops, or tracking history, by load number, reference, customer, carrier or lane.
---

# Find and track a load

Nexus holds the load; iTracker holds its live tracking. Every call runs as the signed-in user, so only loads that user can see are returned.

## 1. Find the load in Nexus

- Known Nexus load number: `nexus_query` with `load(id: …)`.
- Anything else (customer PO, BOL, PRO or other reference, customer, carrier, lane, status): use `loads(...)`.
  - It is paginated: pass `first` (keep it small, e.g. 10) and `page`, and select `data { … }` plus `paginatorInfo { total hasMorePages }`.
  - Filter with `where: { column: …, operator: …, value: … }` using `LoadFilters` columns, e.g. `CONCATENATED_REFERENCES` with `LIKE` and `%value%` for a reference, `STATUS`, `ORIGIN_PLACE`, `DESTINATION_PLACE`.
  - Filter by related records with `hasClient`, `hasCarrier`, `hasStops` and similar arguments.
- If several loads match, list them briefly (id, status, origin → destination, pickup date) and ask which one.

Use `nexus_search_schema` and `nexus_describe_types` to confirm field and filter names before writing the query, and select only the fields you need: `id`, `status`, `itracker_reference_id`, client and carrier names, and the stops with their appointment and arrival times.

## 2. Get live tracking from iTracker

- `itracker_reference_id` on the Nexus load is the iTracker load tracker id. If it is empty, the load is not tracked in iTracker; say so and report from Nexus data only.
- `itracker_query` with `loadTracker(id: …)`, selecting `status`, `eta_at`, `is_delayed`, `delay_in_minutes`, `delay_status`, `origin`, `destination`, the stops, the drivers and `alertSummary`.
- For the movement trail use `checkpoints(id: …)`. For the tracking timeline use `events(...)`; describe its arguments first with `itracker_describe_types`.

## 3. Answer

Lead with the answer: where the load is, whether it is on time, and the ETA to the next stop, with times in the stop's local timezone. Then add the supporting detail: last checkpoint and when it was recorded, delay reason, and any open alerts. Say clearly when tracking data is stale or missing rather than guessing.

iTracker is read-only here. To change anything on a load, use the Nexus tools and follow the confirmation rule in the create-load skill.
