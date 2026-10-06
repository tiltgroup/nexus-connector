---
name: find-loads
description: Find and list Nexus loads (shipments) by status, customer, carrier, lane, pickup or delivery date, open alerts, coverage, or anything scheduled today. Use when the user asks which loads match some criteria, for a list or count of loads, or "what's moving/at risk/uncovered".
---

# Find loads

## Build the query

- Add only the filters the user asked for.
- To filter by a company (customer or carrier), look the company up first and filter by its id; names rarely match exactly.
- Results are paginated. Ask for a small page (10–25) and the total count, so you can say how many matched.
- Select only what the answer needs: the load id, status, origin and destination with their appointments, customer and carrier.

## Answer

- Give the count first ("14 loads are in transit, showing the first 10"), then a compact table: load id, status, origin → destination, pickup and delivery appointments, customer, carrier.
- Offer the next page when there are more results; don't fetch every page unprompted.
- To go deeper on one load, use the track-load skill.
