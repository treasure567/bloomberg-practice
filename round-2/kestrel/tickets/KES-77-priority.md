# KES-77: Time priority violated at a price level

## Report

When two resting orders sit at the same price, an incoming order matches the newer one first.
Traders who posted earlier at a price are being skipped, which breaks the fairness guarantee of
the book.

## Acceptance criteria

- at equal price, the earliest-resting order fills first (FIFO);
- best-price priority across price levels is preserved;
- the fix is in how the resting side is ordered for matching, not a special case;
- add a test with two same-price asks where the earlier one must fill first.

Do not change validation or the cancel path as part of this ticket.
