# TUN-1: Rounding floors instead of rounding to nearest

## Report

Prices are always rounding down. `nearest_multiple` uses floor division, so a price above a tick
is pulled down to the tick below instead of to the nearest one.

## Acceptance criteria

- `round_to_tick(103, 5)` is 105 and `round_to_tick(108, 5)` is 110;
- a halfway value rounds up: `round_to_tick(1025, 50)` is 1050;
- exact multiples are unchanged;
- add tests for rounding up, rounding to nearest, and the tie case.

Keep the public function `round_to_tick`.
