# CAL-TICKET: high-tier requests lose their slot

## Report

Executive assistants report that a STANDARD request sometimes wins a slot over an EXECUTIVE one.
Scheduling is meant to prefer the higher business tier, breaking ties in favour of the earlier
submission. The relevance scorer is a deterministic stand-in; the ranking it produces is what the
scheduler consumes.

## Acceptance criteria

- among requests contending for a slot, the higher `business_tier` is scheduled first;
- equal tiers are ordered by earlier `submitted_at`;
- the fix lives in the ranking, not in a special case inside the scheduler loop;
- add a test where an EXECUTIVE and a STANDARD request contend and the EXECUTIVE wins.

Do not change persistence or the request intake path as part of this ticket.
