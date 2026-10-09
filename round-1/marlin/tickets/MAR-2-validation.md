# MAR-2: Oversell and malformed fills are not rejected

## Report

Selling more than is held drives the position negative (and divides by zero at a zero quantity),
and a fill missing a field or carrying a non-positive quantity or price fails deep in the code
with an unclear error.

## Acceptance criteria

- selling more than the held quantity raises `SettlementError`; the position is unchanged;
- a fill with a missing field or a non-positive quantity or price raises `SettlementError`;
- the errors are raised up front, before any state is mutated;
- add tests for an oversell and for a malformed fill.

Do not change the PnL calculation as part of this ticket.
