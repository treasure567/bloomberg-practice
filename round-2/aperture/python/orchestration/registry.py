from __future__ import annotations

from typing import Dict

from .errors import UnknownJob
from .models import Job, JobStatus


class JobRegistry:
    def __init__(self) -> None:
        self._jobs: Dict[str, Job] = {}

    def register(self, job_id: str) -> Job:
        job = Job(job_id)
        self._jobs[job_id] = job
        return job

    def get(self, job_id: str) -> Job:
        if job_id not in self._jobs:
            raise UnknownJob(job_id)
        return self._jobs[job_id]

    def status(self, job_id: str) -> JobStatus:
        return self._jobs[job_id].status
