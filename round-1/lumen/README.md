# Amount Split

Welcome to the payouts utilities team. This module splits a total amount (integer cents) among n
recipients as evenly as possible; remainder cents go to the earliest recipients so the parts sum
exactly to the total.

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
remainder.py  distribute (hand out base amounts plus the remainder)
split.py      split_amount
tests/        shipped regression tests
tickets/      reported work
```

## Product rules already agreed

- the parts are as even as possible and sum exactly to the total;
- remainder cents go to the earliest recipients, one extra cent each;
- money is integer cents.
