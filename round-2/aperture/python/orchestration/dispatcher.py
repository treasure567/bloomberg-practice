from __future__ import annotations

from typing import List, Optional

from .models import JobStatus
from .queue import ReadyQueue
from .registry import JobRegistry


class Dispatcher:
    def __init__(self, queue: ReadyQueue, registry: JobRegistry, max_retries: int = 3) -> None:
        self.queue = queue
        self.registry = registry
        self.max_retries = max_retries
        self._dead: List[str] = []

    def dequeue(self) -> Optional[str]:
        job_id = self.queue.peek()
        if job_id is None:
            return None
        self.registry.get(job_id).status = JobStatus.INFLIGHT
        return job_id

    def ack(self, job_id: str) -> None:
        self.registry.get(job_id).status = JobStatus.DONE

    def nack(self, job_id: str) -> None:
        job = self.registry.get(job_id)
        self.queue.remove(job_id)
        if job.attempts > self.max_retries:
            job.status = JobStatus.DEAD
            self._dead.append(job_id)
        else:
            job.status = JobStatus.READY
            self.queue.push(job_id)

    def dead_letters(self) -> List[str]:
        return list(self._dead)
