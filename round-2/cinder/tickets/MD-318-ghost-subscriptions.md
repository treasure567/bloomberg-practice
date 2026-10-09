# MD-318: Unsubscribe does not stop callbacks

## Report

After a client unsubscribes it still receives quote callbacks, and the subscription list grows
without bound. Clients that come and go are slowly leaking memory and getting data they no longer
want.

## Acceptance criteria

- after `unsubscribe(symbol, token)`, publishing to that symbol does not call the removed callback;
- the removed subscription is actually dropped from the registry;
- other subscriptions on the same symbol are unaffected;
- add a test that subscribes, unsubscribes, publishes, and asserts no delivery.

Do not change the store or the sequence logic as part of this ticket.
