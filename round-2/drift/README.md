# Fulfillment Service

Welcome to the team that promises stock to orders. A catalog of SKUs, physical on-hand inventory,
and a reservation book combine into an availability view: what can still be promised is the
on-hand count minus what is already reserved.

This repository has three reported problems in `tickets/`. Your interviewer will tell you which
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
fulfillment/
  models.py        domain types (Sku, Reservation)
  errors.py        ValidationError, UnknownSku, OutOfStock
  catalog.py       the SKU catalog (add / exists / require)
  inventory.py     physical on-hand counts per SKU
  reservations.py  the reservation book (place / release / reserved)
  service.py       FulfillmentService: available(), reserve(), release()
tests/             shipped regression tests
tickets/           reported work
```

## Product rules already agreed

- availability is on-hand minus active reservations;
- a reservation is never granted beyond availability;
- releasing a reservation returns its stock to availability;
- an unknown SKU is rejected at the boundary.
