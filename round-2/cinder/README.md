# Market Data Service

Welcome to the team that distributes market data. The service keeps the latest quote per symbol,
built from a snapshot plus incremental updates, and fans quotes out to subscribers. Every update
carries a monotonically increasing sequence number (`seq`) per symbol.

This repository has four reported problems in `tickets/`. Your interviewer will tell you which
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
market_data/
  models.py         domain types (Quote)
  store.py          latest quote per symbol
  sequencer.py      tracks the highest seq per symbol (gap / staleness detection)
  feed.py           applies snapshots and incremental deltas
  subscriptions.py  the subscription hub (subscribe / unsubscribe / publish)
  service.py        MarketDataService: ties store, feed, and the hub together
tests/              shipped regression tests
tickets/            reported work
```

## Product rules already agreed

- updates may arrive out of order; a quote with a lower-or-equal `seq` must not overwrite a newer one;
- a delta only makes sense on top of a base snapshot;
- unsubscribing stops delivery and frees the subscription;
- one subscriber's failure must not affect delivery to the others.
