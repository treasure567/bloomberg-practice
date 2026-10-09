from __future__ import annotations

from typing import List

from policy import delay_for


def backoff_delays(base: int, attempts: int, max_delay: int) -> List[int]:
    return [delay_for(base, a, max_delay) for a in range(1, attempts + 1)]
