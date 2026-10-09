# KES-83: Partial fills discard the remainder

## Report

A partial fill removes the whole resting order instead of reducing its quantity, so the unfilled
remainder vanishes from the book. Liquidity disappears after a small incoming order.

## Acceptance criteria

- a partial fill leaves the resting order with its remaining quantity still available;
- a fully-filled resting order is removed;
- a later incoming order can match the remaining quantity;
- add a test: rest 10, fill 4, then fill 6 and assert both trades occur.

Do not change price-time ordering as part of this ticket.
