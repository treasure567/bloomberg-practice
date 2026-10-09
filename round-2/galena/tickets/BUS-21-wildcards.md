# BUS-21: Wildcard subscriptions never match

## Report

Subscribers using `"px.*"` or `"*"` receive nothing. Only exact-topic subscriptions get messages,
so every wildcard consumer is silently broken.

## Acceptance criteria

- `"px.*"` matches `"px.AAPL"` and any single trailing segment under `px`;
- `"*"` matches every topic;
- an exact pattern still matches only its exact topic;
- add a test that subscribes with `"px.*"` and asserts delivery of a `"px.AAPL"` message.

Do not change the subscription registry or the router loop as part of this ticket.
