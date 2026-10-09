# Cache Tier

Welcome to the team that owns the caching tier. A capacity-bounded LRU cache serves hot values;
both `get` and `put` count as using a key, and when capacity is exceeded the least-recently-used
entry is evicted.

This repository has three reported problems in `tickets/`. Your interviewer will tell you which
ticket to start with. You are not expected to finish every ticket.

You may use the available AI assistant and normal repository tools. Treat the assistant like a
junior developer: establish a plan, inspect its work, run the tests, and retain ownership of the
result.

## Run the tests

This pack has the same problem in three languages (`python/`, `cpp/`, `java/`). Pick one:

```bash
# Python
cd python && pytest -q

# C++
cd cpp && make test          # or: g++ -std=c++17 tests.cpp -o tests && ./tests

# Java
cd java && javac *.java && java Tests
```

All three implement the same spec and the same planted bugs; every test fails until you fix them.

## Repository map

```text
cache/
  lru.py       LRUCache: get / put with LRU eviction
  errors.py    CacheError
  service.py   CacheService: get / put
tests/         shipped regression tests
tickets/       reported work
```

## Product rules already agreed

- the cache never exceeds its capacity;
- `get` and `put` both mark a key as most-recently-used;
- on overflow, the least-recently-used key is evicted;
- updating an existing key refreshes it and does not grow the cache.
