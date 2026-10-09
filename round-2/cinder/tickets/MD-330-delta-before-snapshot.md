# MD-330: Deltas applied without a base snapshot

## Report

A delta for a symbol that has no prior snapshot silently fabricates a 0/0 base quote instead of
failing. Downstream consumers then see a bogus zero price. A delta only makes sense on top of a
snapshot.

## Acceptance criteria

- `apply_delta` for a symbol with no snapshot raises `LookupError`;
- a delta applied after a snapshot still works and carries forward unset fields;
- no fabricated 0/0 quote ever enters the store;
- add a test that applies a delta with no prior snapshot and asserts it raises.

Do not change the subscription code as part of this ticket.
