---
name: quote-and-book
description: Get LTL freight quotes in Nexus, compare carrier rates and transit times, and book the chosen quote; also look up lane pricing and historical rates for truckload pricing. Use when the user asks for a quote, rate, price or transit time on a lane, or wants to book a quote.
---

# Quote and book

## Work from the live schema

The Nexus API changes over time, so don't assume query, mutation, input or status names. Search the schema (for example `ltl quote`, `lane pricing`, `historical rate`), describe the types you find, and use exactly what they say. When a call returns an error, read it, describe the type it names and fix the request instead of guessing.

## Truckload rates (read-only)

For a truckload price check, use the pricing data the schema offers for a lane, such as lane pricing and historical rates. Present the rate range with its source and date, and say how confident it is when the data is thin.

## LTL quotes

1. **Request (changes data).** An LTL quote request usually needs the customer, pickup and delivery locations, freight class, and commodities with weight, pieces and dimensions; the request input type is the authority. Show the request to the user and get confirmation before sending it.
2. **Wait for rates.** Carrier rates arrive shortly after the request. Read the quote request's status and its quotes. If no rates have arrived yet, tell the user and check again when they ask; don't poll in a tight loop.
3. **Compare.** List the quotes by total cost with the carrier, transit time, estimated delivery, service level and expiry. Flag quotes that expire soon.
4. **Book (changes data).** Booking commits the shipment with the carrier. Restate the quote: carrier, total cost, transit time and pickup date. Wait for an explicit yes, then book that exact quote and report the resulting shipment and its status.

If booking fails, say so and offer the next-best quote; never book a different quote without asking.

Link every load you mention to Nexus: `https://nexus.tiltgroup.com/shipments/<id>`.
