# MD-324: One bad subscriber blocks the rest

## Report

If one subscriber's callback raises, later subscribers for the same symbol receive nothing. A
single misbehaving client is taking down fan-out for everyone on that symbol.

## Acceptance criteria

- an exception in one callback does not stop delivery to the others;
- the policy for a failing callback is explicit (dropped) rather than accidental;
- delivery order for healthy subscribers is preserved;
- add a test with one raising subscriber and one healthy subscriber that still receives the quote.

Do not change the store or the sequence logic as part of this ticket.
