# APT-415: Acked jobs can be handed out again

## Report

A completed job can still be dequeued. After `ack`, a job should be out of circulation; instead it
can be redelivered and processed twice.

## Acceptance criteria

- after `ack`, `dequeue` never returns that job again;
- the job's status reflects completion;
- acking a job that is not in flight does not corrupt the queue;
- add a test that enqueues, dequeues, acks, and asserts the next `dequeue` is `None`.

Do not change the retry or dead-letter logic as part of this ticket.
