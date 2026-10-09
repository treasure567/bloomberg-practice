# SESS-24: Expired sessions are never reclaimed

## Report

The session store grows without bound. `cleanup` does nothing, so expired sessions accumulate and
leak memory over time.

## Acceptance criteria

- `cleanup(now)` removes every session with `now >= expiry`;
- sessions that are not yet expired are kept;
- the store size reflects only live sessions after cleanup;
- add a test that creates a session, cleans up at its expiry, and asserts it is gone and size is 0.

Do not change the expiry boundary rule as part of this ticket.
