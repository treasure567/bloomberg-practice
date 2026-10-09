# VES-1: Exponent off by one and cap ignored

## Report

Backoff delays start too high and grow without bound. The per-attempt delay uses `2**attempt`
instead of `2**(attempt-1)`, and `max_delay` is never applied.

## Acceptance criteria

- `backoff_delays(1, 4, 100)` is `[1, 2, 4, 8]`;
- `backoff_delays(1, 5, 5)` is `[1, 2, 4, 5, 5]` (capped at max_delay);
- `backoff_delays(3, 3, 100)` is `[3, 6, 12]`;
- add a test that exercises the cap.

Keep the public function `backoff_delays`.
