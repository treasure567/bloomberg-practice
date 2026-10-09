# Interval Merge

Welcome to the scheduling utilities team. This module merges closed integer intervals
`[start, end]`. Overlapping and touching intervals merge; the input is unsorted and the output
must be sorted by start.

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
ordering.py   by_start (orders intervals before merging)
intervals.py  merge
tests/        shipped regression tests
tickets/      reported work
```

## Product rules already agreed

- intervals are closed: `[1,2]` and `[2,3]` touch and merge into `[1,3]`;
- overlapping intervals merge;
- the input is unsorted; the output is sorted by start.
