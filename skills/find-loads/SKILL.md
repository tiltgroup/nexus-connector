---
name: find-loads
description: Find and list Nexus loads (shipments) by status, customer, carrier, lane, pickup or delivery date, open alerts, coverage, or anything scheduled today. Use when the user asks which loads match some criteria, for a list or count of loads, or "what's moving/at risk/uncovered".
---

# Find loads

`loads(...)` through `nexus_query` returns only loads the signed-in user can see. It is paginated: always pass `first` (10–25) and `page`, and select `paginatorInfo { total hasMorePages }` so you can say how many matched.

## Base query

```graphql
query FindLoads($first: Int!, $page: Int) {
  loads(first: $first, page: $page, orderBy: [{ column: ORIGIN_APPOINTMENT_AT_UTC, order: ASC }]) {
    paginatorInfo { total hasMorePages }
    data {
      id status
      origin { place region_code appointment_at }
      destination { place region_code appointment_at }
      client { name }
      carrier { name }
    }
  }
}
```

Add only the filter arguments the user asked for. Filters combine with AND.

## Filter templates

Filters use `{ column, operator, value }`. Operators: `EQ`, `NEQ`, `GT`, `GTE`, `LT`, `LTE`, `LIKE`, `IN`, `NOT_IN`, `BETWEEN`, `IS_NULL`, `IS_NOT_NULL`. Combine several on one argument with `AND: [ … ]`. Status values are lowercase strings such as `open`, `covered`, `dispatched`, `at_pickup`, `loaded`, `in_transit`, `at_consignee`, `delivered`.

| User asks for | Argument |
|---|---|
| A status or several | `where: { column: STATUS, operator: IN, value: ["dispatched", "in_transit"] }` |
| A reference (PO, BOL, PRO, pickup number) | `where: { column: CONCATENATED_REFERENCES, operator: LIKE, value: "%12345%" }` |
| Picking up in a date range | `where: { column: ORIGIN_APPOINTMENT_AT_UTC, operator: BETWEEN, value: ["2026-10-06T00:00:00Z", "2026-10-07T00:00:00Z"] }` |
| Delivering in a date range | the same with `DESTINATION_APPOINTMENT_AT_UTC` |
| A lane | `where: { AND: [{ column: ORIGIN_REGION_CODE, operator: EQ, value: "TX" }, { column: DESTINATION_REGION_CODE, operator: EQ, value: "GA" }] }` (or `ORIGIN_PLACE` / `DESTINATION_PLACE` for cities) |
| Anything scheduled today | `isScheduledToday: true` |
| No carrier yet | `isUncovered: true` |
| Open alerts | `hasAlerts: { column: IS_RESOLVED, operator: EQ, value: false }` |
| Major or critical open alerts | `hasAlerts: { AND: [{ column: IS_RESOLVED, operator: EQ, value: false }, { column: SEVERITY, operator: GTE, value: 2 }] }` (severity is stored as a number: 0 low, 1 minor, 2 major, 3 critical) |
| A customer or carrier | look the company up first, then filter by its id: `hasClient: { column: ID, operator: EQ, value: <id> }` or `hasCarrier: { … }` |

`LIKE` is case-sensitive. For a customer or carrier name, search `clients` or `carriers` first and filter by id rather than guessing the capitalisation.

For any other filter, describe `LoadFilters` and the related `…Filters` enums with `nexus_describe_types`.

## Answer

- Give the count first ("14 loads are in transit, showing the first 10"), then a compact table: load id, status, origin → destination, pickup and delivery appointments, customer, carrier.
- Link each load to Nexus: `https://nexus.tiltgroup.com/shipments/<id>`.
- Offer the next page when `hasMorePages` is true; don't fetch every page unprompted.
- To go deeper on one load, use the track-load skill.
