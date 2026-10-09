# KES-90: Cancel does not remove resting orders

## Report

`cancel` is a no-op: a cancelled order still rests and still matches. Traders are getting fills on
orders they pulled.

## Acceptance criteria

- after `cancel(order_id)`, the order no longer rests on either side;
- a subsequent crossing order does not match the cancelled order;
- cancelling an unknown order id is a no-op, not an error;
- add a test that rests an order, cancels it, and asserts a crossing order produces no trade.

Do not change the matching algorithm as part of this ticket.
