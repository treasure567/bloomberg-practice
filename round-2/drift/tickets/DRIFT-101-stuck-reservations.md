# DRIFT-101: Released reservations keep holding stock

## Report

`release` does not actually free a reservation, so availability never recovers after a hold is
cancelled. Stock stays locked away from new orders.

## Acceptance criteria

- after `release`, the reservation no longer counts toward `reserved` or `available`;
- releasing an unknown reservation id is a no-op, not an error;
- availability returns to on-hand minus the remaining active reservations;
- add a test that reserves, releases, and asserts availability is restored.

Do not change the oversell check as part of this ticket.
