---
name: quote-and-book
description: Get LTL freight quotes in Nexus, compare carrier rates and transit times, and book the chosen quote; also look up lane pricing and historical rates for truckload pricing. Use when the user asks for a quote, rate, price or transit time on a lane, or wants to book a quote.
---

# Quote and book

## Truckload rates (read-only)

For a truckload price check, use the existing pricing data: `lanePricing(id)`, `lanePricings(...)` (search history) and `shipmentHistoricalRates(...)`. Describe their arguments with `nexus_describe_types` first. Present the rate range with its source and date, and say how confident it is when the data is thin.

## LTL quotes

1. **Request.** An LTL quote request needs the customer, pickup and delivery stops, freight class, and commodities with weight, pieces and dimensions. Describe `LtlQuoteRequestInput` (or `LtlQuickQuoteRequestInput` for a quick quote) before building it. Show the request to the user and get confirmation, then call `createLtlQuoteRequest` (or `createQuickLtlQuoteRequest`) through `nexus_mutate`.
2. **Wait for rates.** Carrier rates arrive shortly after the request. Read `ltlQuoteRequest(id)` for its `status` (`REQUESTED` → `QUOTED`) and `ltlQuotes(id: <request id>)` for the rates. If no rates have arrived yet, tell the user and check again when they ask; don't poll in a tight loop.
3. **Compare.** List the quotes by `totalCost` with `carrierName`, `transitDays`, `estimatedDeliveryAt`, `service` and `expiresAt`. Flag quotes that expire soon and interline quotes.
4. **Book (changes data).** Booking commits the shipment with the carrier. Restate the quote: carrier, total cost, transit time and pickup date. Wait for an explicit yes, then call `bookLtlQuote(input: { id: <quote id>, carrier: … })`. Report the booked shipment from `ltlQuoteRequest(id) { status bookedShipment { id status } }`.

If booking fails (status `BOOKING_FAILED`), say so and offer the next-best quote; never book a different quote without asking.

Link every load you mention to Nexus: `https://nexus.tiltgroup.com/shipments/<id>`.
