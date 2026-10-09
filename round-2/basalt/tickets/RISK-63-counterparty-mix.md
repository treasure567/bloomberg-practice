# RISK-63: Counterparties share a position

## Report

Two counterparties trading the same symbol are being netted together, so one counterparty's
exposure bleeds into another's. Positions are keyed only by symbol.

## Acceptance criteria

- positions are isolated per `(counterparty, symbol)`;
- the same symbol under two counterparties yields two independent nets;
- a query for one counterparty never reflects another's trades;
- add a test with two counterparties in the same symbol and assert independence.

Do not change the sign handling or idempotency as part of this ticket.
