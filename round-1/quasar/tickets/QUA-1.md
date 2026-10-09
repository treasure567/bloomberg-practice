# QUA-1: Tier boundaries and fee floor are wrong

## Report

Fees are wrong at the tier edges and for small amounts. The tier comparisons use `<=`, so a
boundary amount falls into the higher-rate tier, and there is no minimum-fee floor, so small
transactions are charged less than the agreed minimum.

## Acceptance criteria

- `fee_for(10000)` is 100 (the boundary is in the 1% tier) and `fee_for(100000)` is 500;
- `fee_for(2000)` is 50 (the floor, since 2% is 40);
- fees remain integer cents;
- add tests for both tier boundaries and for the floor.

Keep the public function `fee_for`.
