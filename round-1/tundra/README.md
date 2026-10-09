# Tick Rounding

Welcome to the pricing utilities team. This module rounds a price (integer cents) to the nearest
tick size (integer cents); ties round up to the larger multiple.

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
rounding.py  nearest_multiple (round to nearest multiple of a step)
tick.py      round_to_tick
tests/       shipped regression tests
tickets/     reported work
```

## Product rules already agreed

- round to the nearest multiple of the tick size;
- a value exactly halfway rounds up to the larger multiple;
- exact multiples are unchanged.
