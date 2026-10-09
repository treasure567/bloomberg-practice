# Rate Limiter

Welcome to the gateway team. This module is a fixed-window rate limiter: at most `limit` calls per
window of `window` ticks, windows being `[k*window, (k+1)*window)`.

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
window.py   window_of (which fixed window a time falls into)
limiter.py  FixedWindowLimiter.allow
tests/      shipped regression tests
tickets/    reported work
```

## Product rules already agreed

- at most `limit` calls are allowed per fixed window;
- the counter resets at each window boundary;
- `allow(now)` returns True when permitted and False when the limit is exceeded.
