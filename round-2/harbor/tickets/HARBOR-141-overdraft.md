# HARBOR-141: Accounts can be overdrawn past their holds

## Report

Transfers go through even when the amount is larger than the funds actually available on the
source account. Available funds are the ledger balance minus any active holds; a transfer above
that should be refused and leave the ledger untouched.

## Acceptance criteria

- a transfer greater than `available(src)` raises `InsufficientFunds`;
- a rejected transfer writes no ledger entry and moves no money;
- active holds reduce the amount that can be transferred;
- add a test that places a hold, then attempts a transfer that only fails once the hold is counted.

Do not redesign the ledger or the hold model as part of this ticket.
