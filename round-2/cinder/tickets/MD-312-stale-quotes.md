# MD-312: Stale updates overwrite fresh quotes

## Report

Quotes occasionally flicker back to an older price. Updates can arrive out of order because of
retransmits and multiple feed handlers. An update whose `seq` is not greater than the stored
quote's `seq` must be ignored.

## Acceptance criteria

- applying a quote whose `seq` is not greater than the stored one is a no-op;
- a genuinely newer `seq` still updates the quote;
- the rule is enforced in the store, the single source of truth, not at each call site;
- add a test that applies a newer then an older update and asserts the newer survives.

Do not change the subscription or feed code as part of this ticket.
