# CACHE-14: get does not refresh recency

## Report

Reading a key does not mark it as recently used, so a frequently-read key can be evicted while
keys that are never touched survive. Cache hit rates are worse than they should be.

## Acceptance criteria

- a key read with `get` is marked most-recently-used and survives the next eviction;
- an untouched key is evicted before a recently-read one;
- the value returned by `get` is unchanged;
- add a test that reads a key and then forces an eviction, asserting the read key survives.

Do not change the eviction direction as part of this ticket.
