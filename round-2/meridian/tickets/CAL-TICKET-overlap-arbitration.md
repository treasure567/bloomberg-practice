# CAL-TICKET: meetings booked over protected commitments

## Report

Employees are being double-booked: a scheduled meeting lands in a slot already held by a protected
calendar event. Requests are supposed to be scheduled in batches *around* protected commitments,
never on top of them.

## Acceptance criteria

- `schedule_batch` never accepts a request that overlaps a protected event;
- half-open intervals hold: a request ending when a protected block starts is fine;
- the invariant holds regardless of the order requests are considered;
- add a test with one protected event and a request that overlaps it.

State the overlap invariant in your own words before changing code. Do not change the scoring
model as part of this ticket.
