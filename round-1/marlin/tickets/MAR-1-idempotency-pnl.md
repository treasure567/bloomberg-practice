# MAR-1: Duplicate fills and wrong realized PnL

## Report

Two correctness problems in settlement. Resent fills (same `trade_id`) are applied twice, inflating
positions. And realized PnL on a sell uses the most recent purchase price instead of the weighted
average cost, so PnL does not match a hand calculation after staggered buys.

## Acceptance criteria

- applying two fills with the same `trade_id` leaves the position as if applied once;
- realized PnL on a sell is `(sell_price - avg_cost) * qty`, where `avg_cost` is the weighted
  average over the held quantity;
- cost basis is reduced consistently when a position is sold down;
- add a test with two buys at different prices and a sell, asserting the realized PnL.

Do not change the validation rules as part of this ticket.
