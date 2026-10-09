# SESS-18: touch does not extend a session

## Report

Active users are being logged out on schedule even though they are still using the app. `touch`
is a no-op, so a session never gets its life extended.

## Acceptance criteria

- after `touch(sid, now, ttl)`, the session is valid until `now + ttl`;
- touching an unknown session id is a no-op, not an error;
- a touched session that later passes its new expiry is still expired;
- add a test that touches a session and asserts it survives past its original expiry.

Do not change the expiry boundary rule as part of this ticket.
