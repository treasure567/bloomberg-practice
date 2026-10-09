# Payments Service

Welcome to the team that runs money movement for the platform. Accounts hold balances in a
double-entry ledger; funds can be reserved with holds and moved between accounts with idempotent
transfers. Every amount is an integer number of cents.

This repository has four reported problems in `tickets/`. Your interviewer will tell you which
ticket to start with. You are not expected to finish every ticket.

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
payments/
  models.py      domain types (Account, LedgerEntry, Hold)
  errors.py      ValidationError, UnknownAccount, InsufficientFunds
  accounts.py    the account store (open / exists / require)
  ledger.py      append-only double-entry ledger; balance = debits - credits
  holds.py       funds reserved against an account but not yet moved
  transfers.py   available() and the idempotent transfer() with a funds check
  service.py     PaymentsService: deposit, place_hold, release_hold, transfer, balance, available
tests/           shipped regression tests
tickets/         reported work
```

## Product rules already agreed

- all amounts are integer cents; floating point must not enter the ledger;
- the ledger is double-entry: every posting debits one account and credits another, and the sum
  of all balances is always zero;
- available funds are the ledger balance minus active holds;
- transfers are idempotent on `transfer_id`;
- a rejected transfer writes no ledger entry.
