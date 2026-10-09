# CACHE-9: Eviction drops the wrong entry

## Report

Under load the cache is evicting the entry that was just inserted instead of the
least-recently-used one. Hot data is being thrown away while cold data survives.

## Acceptance criteria

- on overflow, the least-recently-used key is the one evicted;
- the most-recently inserted key stays in the cache;
- capacity is never exceeded;
- add a test: capacity 2, put a, b, c, and assert `a` is gone while `b` and `c` remain.

Do not change the `get` recency behaviour as part of this ticket.
