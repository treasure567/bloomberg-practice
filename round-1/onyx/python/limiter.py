from __future__ import annotations

from window import window_of


class FixedWindowLimiter:
    def __init__(self, limit: int, window: int) -> None:
        self.limit = limit
        self.window = window
        self._cur = -1
        self._count = 0

    def allow(self, now: int) -> bool:
        w = window_of(now, self.window)
        if w != self._cur:
            self._cur = w
            self._count = 0
        if self._count <= self.limit:
            self._count += 1
            return True
        return False
