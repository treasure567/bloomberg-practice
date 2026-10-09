# Retry Backoff

Welcome to the resilience utilities team. This module computes retry backoff delays: for attempts
1..n, `base * 2**(attempt-1)`, capped at `max_delay`.

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
policy.py   delay_for (per-attempt delay)
backoff.py  backoff_delays
tests/      shipped regression tests
tickets/    reported work
```

## Product rules already agreed

- the delay for 1-based attempt a is `base * 2**(a-1)`;
- every delay is capped at `max_delay`;
- the result has one entry per attempt.
