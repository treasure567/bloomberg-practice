from __future__ import annotations

import enum
from dataclasses import dataclass


class JobStatus(enum.Enum):
    READY = "ready"
    INFLIGHT = "inflight"
    DONE = "done"
    DEAD = "dead"


@dataclass
class Job:
    job_id: str
    status: JobStatus = JobStatus.READY
    attempts: int = 0
