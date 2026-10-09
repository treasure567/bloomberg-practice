# ONY-1: The limiter allows one call too many

## Report

Clients are getting through slightly more often than they should. The limiter permits `limit + 1`
calls in a window because the count check is off by one.

## Acceptance criteria

- with limit 2, window 10: `allow(0)` and `allow(1)` are True and `allow(2)` is False;
- the counter still resets at a new window (times 0,1,2,10 give `[True, True, False, True]`);
- the limit is respected exactly, with no off-by-one;
- add a test asserting the `(limit+1)`-th call in a window is rejected.

Keep the public class `FixedWindowLimiter` and its `allow` signature.
