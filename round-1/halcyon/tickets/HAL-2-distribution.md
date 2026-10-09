# HAL-2: Distribution over-pays the pot

## Report

The pot is paying out more than it holds. Every tier is paid independently, so a jackpot (5-match)
winner does not consume the pot, and tier splits silently drop remainder cents.

## Acceptance criteria

- when a 5-match winner exists, only that tier is paid (100% of the pot) and lower tiers get nothing;
- a tier's split conserves cents exactly: the sum of payouts equals the tier amount;
- unawarded money is reported as rollover;
- add a test with a 5-match winner present that asserts lower tiers receive nothing.

Do not change code generation or match scoring as part of this ticket.
