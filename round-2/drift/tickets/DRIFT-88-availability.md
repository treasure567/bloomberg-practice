# DRIFT-88: Availability ignores reservations

## Report

The same stock is being promised twice. `available(sku)` returns the physical on-hand count and
ignores reservations that are already holding some of it, so two orders can each be told the stock
is free.

## Acceptance criteria

- `available(sku)` equals on-hand minus active reservations for that SKU;
- reserving stock immediately lowers availability by the reserved amount;
- availability for other SKUs is unaffected;
- add a test that reserves part of the stock and asserts availability drops.

Do not change the inventory or catalog modules as part of this ticket.
