# Order Identifiers

Welcome to the team that mints order identifiers. A sequence number becomes
`ORD-<8-digit zero-padded>-<check digit>`, where the check digit is the sum of the eight body
digits modulo 10.

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
checksum.py  check_digit (sum of body digits mod 10)
codes.py     format_code and is_valid
tests/       shipped regression tests
tickets/     reported work
```

## Product rules already agreed

- the body is an 8-digit zero-padded sequence number;
- the check digit is the sum of the body digits modulo 10;
- `is_valid` accepts a well-formed code with a correct check digit and rejects anything else.
