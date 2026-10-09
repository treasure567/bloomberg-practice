# HARBOR-158: The ledger does not balance

## Report

Account balances do not reconcile. The sum of all balances drifts away from zero, and a transfer
appears to increase the sender's balance instead of decreasing it. In a double-entry ledger the
debit side increases while the credit side decreases by the same amount.

## Acceptance criteria

- a transfer decreases the sender and increases the receiver by the same amount;
- after any sequence of postings the sum of all account balances is zero;
- deposits and transfers both preserve this invariant;
- add a test that asserts conservation after a deposit and a transfer.

Do not change the public API of the ledger as part of this ticket.
