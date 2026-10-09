from __future__ import annotations

from typing import List, Optional


class ReadyQueue:
    """FIFO queue of job ids waiting to be dispatched."""

    def __init__(self) -> None:
        self._items: List[str] = []

    def push(self, job_id: str) -> None:
        self._items.append(job_id)

    def pop(self) -> Optional[str]:
        if not self._items:
            return None
        return self._items.pop(0)

    def peek(self) -> Optional[str]:
        return self._items[0] if self._items else None

    def remove(self, job_id: str) -> None:
        if job_id in self._items:
            self._items.remove(job_id)

    def __len__(self) -> int:
        return len(self._items)
