# APT-410: Jobs are handed out repeatedly

## Report

Workers keep processing the same job. `dequeue` returns a job but does not remove it from the
ready queue or mark it in flight, so several workers pick up the same work at once.

## Acceptance criteria

- a dequeued job is removed from the ready queue;
- the next `dequeue` returns a different job, or `None` when the queue is empty;
- the dequeued job is marked in flight in the registry;
- add a test that enqueues one job and asserts the second `dequeue` returns `None`.

Do not change the retry or dead-letter logic as part of this ticket.
