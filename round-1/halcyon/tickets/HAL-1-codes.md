# HAL-1: Codes lose leading zeros and match by digit set

## Report

Two problems with entry codes have been reported. Codes render without zero padding ("42" instead
of "00042"), so "00000" cannot even be represented. And match counting compares the set of digits
rather than their positions, so unrelated codes score as near-winners.

## Acceptance criteria

- a code is always a 5-character zero-padded token;
- match count is positional (digit i equals winning digit i), including repeated digits;
- a code that shares digits but not positions scores low;
- add a test that a positional near-miss (e.g. "54321" vs "12345") counts as one match.

Do not change the payout distribution as part of this ticket.
