# RISK-57: Replayed trades are double-counted

## Report

The same trade sometimes arrives twice from the upstream feed, and the position counts it twice.
Trades must be idempotent on `trade_id`.

## Acceptance criteria

- adding the same `trade_id` twice counts the trade once;
- a genuinely new `trade_id` with the same fields still counts;
- the net reflects exactly one application of a replayed trade;
- add a test that adds the same `trade_id` twice and asserts a single application.

Do not change the sign handling as part of this ticket.
