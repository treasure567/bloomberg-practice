# SESS-12: Sessions live one tick too long

## Report

A session is still considered valid at exactly its expiry tick. The policy should treat a session
as expired once `now >= expiry`, but it uses a strict greater-than, so sessions survive one tick
past their deadline.

## Acceptance criteria

- a session created at 0 with ttl 10 is expired at `now == 10`;
- a session is still valid at `now == 9`;
- the boundary rule lives in the expiry policy, not scattered at call sites;
- add a test that asserts expiry at exactly the expiry tick.

Do not change `touch` or `cleanup` as part of this ticket.
