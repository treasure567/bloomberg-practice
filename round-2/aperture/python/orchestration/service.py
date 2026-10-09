from __future__ import annotations

from typing import List, Optional

from .dispatcher import Dispatcher
from .queue import ReadyQueue
from .registry import JobRegistry


class OrchestrationService:
    def __init__(self, max_retries: int = 3) -> None:
        self.queue = ReadyQueue()
        self.registry = JobRegistry()
        self.dispatcher = Dispatcher(self.queue, self.registry, max_retries)

    def enqueue(self, job_id: str) -> None:
        self.registry.register(job_id)
        self.queue.push(job_id)

    def dequeue(self) -> Optional[str]:
        return self.dispatcher.dequeue()

    def ack(self, job_id: str) -> None:
        self.dispatcher.ack(job_id)

    def nack(self, job_id: str) -> None:
        self.dispatcher.nack(job_id)

    def dead_letters(self) -> List[str]:
        return self.dispatcher.dead_letters()
