# Matching Engine

Welcome to the team that runs the order book. A single-symbol limit order book matches incoming
orders against resting ones with price-time priority: best price first and, within a price level,
oldest order first. Partial fills reduce the resting quantity; the unfilled remainder of an
incoming order rests.

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
matching/
  models.py    domain types (Resting, Trade)
  errors.py    ValidationError
  book.py      the order book: limit() matching and cancel()
  service.py   MatchingService: submit() (validates) and cancel()
tests/         shipped regression tests
tickets/       reported work
```

## Product rules already agreed

- matching is price-time priority: best price first, then oldest resting order (FIFO) at a price;
- a partial fill reduces the resting order's quantity; it is not removed until fully filled;
- the unfilled remainder of an incoming order rests in the book;
- a cancelled order no longer rests and cannot match.
