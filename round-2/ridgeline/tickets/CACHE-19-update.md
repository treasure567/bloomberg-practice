# CACHE-19: Updating a key does not refresh it

## Report

Re-putting an existing key updates its value but not its recency, so a freshly written key can be
evicted before older, untouched ones.

## Acceptance criteria

- updating an existing key makes it most-recently-used;
- updating an existing key does not grow the cache beyond capacity;
- the new value is the one returned on the next `get`;
- add a test that updates a key and then forces an eviction, asserting the updated key survives.

Do not change the eviction direction as part of this ticket.
