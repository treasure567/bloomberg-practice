# BUS-27: Unsubscribe does nothing

## Report

After a client unsubscribes it keeps receiving messages. The registry's remove path compares the
wrong fields, so nothing is ever removed and subscriptions leak.

## Acceptance criteria

- after `unsubscribe(token)`, that subscription no longer receives messages;
- the subscription is actually removed from the registry;
- other subscriptions are unaffected;
- add a test that subscribes, unsubscribes, publishes, and asserts no delivery.

Do not change topic matching or the router loop as part of this ticket.
