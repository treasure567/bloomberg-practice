# Fee Calculation

Welcome to the billing utilities team. This module computes a transaction fee by tier, with a
minimum fee floor. Money is integer cents.

This repository has one reported problem in `tickets/`. You may use the available AI assistant and
normal repository tools. Treat the assistant like a junior developer: establish a plan, inspect its
work, run the tests, and retain ownership of the result.

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
tiers.py  rate_for (tier selection) and MIN_FEE_CENTS
fees.py   fee_for
tests/    shipped regression tests
tickets/  reported work
```

## Product rules already agreed

- tiers: amount < 10000 -> 2%, 10000 <= amount < 100000 -> 1%, amount >= 100000 -> 0.5%;
- the minimum fee is 50 cents;
- fees are integer cents, rounded down, but never below the floor.
