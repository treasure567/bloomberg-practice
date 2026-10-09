# CAL-TICKET: duplicate request after retry

## Report

Occasionally the same meeting request appears twice. It is most common when the requester's
connection is unstable and the client retries before receiving a response. Slow, sequential
retries normally return the original request, so a naive sequential test can pass while the real
problem remains.

## Acceptance criteria

- one requester and idempotency key produce exactly one stored request;
- overlapping submissions return the same request id rather than an internal error;
- the same idempotency key may be used by two different requesters;
- the fast existing lookup may remain, but correctness cannot depend on its timing;
- add a test that sends overlapping submissions, not merely sequential calls.

Do not redesign scheduling or relevance scoring as part of this ticket.
