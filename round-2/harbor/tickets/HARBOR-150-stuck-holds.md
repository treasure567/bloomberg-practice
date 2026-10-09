# HARBOR-150: Released holds still reserve funds

## Report

After a hold is released the reserved funds do not come back: `available` stays low. Merchants
report that a cancelled authorization keeps blocking a customer's balance.

## Acceptance criteria

- after `release_hold`, the hold no longer counts toward `held` or `available`;
- releasing an unknown hold id is a no-op, not an error;
- available funds return to the balance minus the remaining active holds;
- add a test that reserves, releases, and asserts availability is restored.

Do not change the transfer path as part of this ticket.
