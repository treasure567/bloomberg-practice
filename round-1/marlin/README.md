# Trade Settlement

Welcome to the settlement team. The engine applies a batch of trade fills into per-symbol
positions and realized profit and loss. Each fill has `trade_id`, `symbol`, `side` ("buy"/"sell"),
`quantity`, and `price_cents`. Money is integer cents.

This repository has two reported problems in `tickets/`. Your interviewer will tell you which one
to start with. You are not expected to finish every ticket.

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
models.py      Position and the SettlementError type
settlement.py  Blotter (apply) and settle (batch)
tests/         shipped regression tests
tickets/       reported work
```

## Product rules already agreed

- `trade_id` is unique: a resent fill is applied exactly once;
- realized PnL on a sell uses the weighted average cost of the held position, not the last price;
- a position never goes negative; overselling is rejected;
- a malformed fill (missing field, non-positive quantity or price) is rejected at the boundary.
