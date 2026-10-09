# COB-1: Window size and aggregation are wrong

## Report

Rolling statistics are off. The sliding window yields one element too few (size minus one),
`moving_average` floors each result with integer division, and `rolling_max` computes a minimum
instead of a maximum.

## Acceptance criteria

- the window generator yields full windows of the requested size;
- `moving_average([1,2,3,4], 2)` is `[1.5, 2.5, 3.5]` (real-valued);
- `rolling_max([1,3,2,5,4], 2)` is `[3, 3, 5, 5]`;
- add tests for a non-integer average and for `rolling_max`.

Keep the public functions `moving_average` and `rolling_max`.
