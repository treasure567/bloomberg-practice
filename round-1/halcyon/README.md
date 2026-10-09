# Pooled Draw

Welcome to the team that runs the community pooled cash drawing. `CodeIssuer` assigns 5-digit
entry codes and scores positional matches against the winning code; `payouts.distribute` splits
the pot by match-count tiers. All money is integer cents.

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
codes.py     CodeIssuer (issue, match_count) and the Entry type
payouts.py   pot_cents and distribute (tiered payout)
tests/       shipped regression tests
tickets/     reported work
```

## Product rules already agreed

- a code is a 5-character zero-padded token (number 42 is "00042", 0 is "00000");
- a match is positional: digit i of the code equals digit i of the winning code;
- payout by match count as a percent of the pot: 5 -> 100, 4 -> 40, 3 -> 20, 2 -> 5, 1 -> 0;
- a 5-match winner consumes the whole pot; lower tiers pay only when there is no 5-match winner;
- within a tier, winners split equally and leftover cents go to the earliest entries; money is integer cents.
