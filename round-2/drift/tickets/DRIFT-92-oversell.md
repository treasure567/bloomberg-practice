# DRIFT-92: Reservations can oversell

## Report

A reservation larger than what is available succeeds and drives availability negative. Warehouses
are getting orders they cannot fill.

## Acceptance criteria

- reserving more than `available(sku)` raises `OutOfStock`;
- a rejected reservation leaves availability unchanged;
- a reservation exactly equal to availability is allowed;
- add a test that attempts to reserve beyond availability and asserts it raises.

Do not change the reservation-release path as part of this ticket.
