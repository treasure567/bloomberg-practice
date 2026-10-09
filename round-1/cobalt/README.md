# Rolling Statistics

Welcome to the analytics utilities team. This module computes rolling window statistics over a
list of numbers: moving averages and rolling maxima.

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
windows.py  the sliding window generator
stats.py    moving_average and rolling_max
tests/      shipped regression tests
tickets/    reported work
```

## Product rules already agreed

- a window of size k produces one output per full window (length n - k + 1);
- `moving_average` returns real-valued averages (no truncation);
- `rolling_max` returns the maximum of each window.
