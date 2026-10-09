# HARBOR-134: Retried transfers move money twice

## Report

A client that retries `transfer` with the same `transfer_id` moves the funds again. It is most
common when the caller's connection is unstable and it retries before receiving our response. A
slow, sequential retry should simply return without moving money a second time.

## Acceptance criteria

- a transfer with a previously seen `transfer_id` is a no-op after the first application;
- the retried call does not raise; it returns as if the original had succeeded;
- balances reflect exactly one application of the transfer;
- add a test that applies the same transfer twice and asserts the funds moved once.

Do not change the ledger or the hold model as part of this ticket.
