from __future__ import annotations

from typing import List

from windows import windows


def moving_average(values: List[float], size: int) -> List[float]:
    return [sum(w) // len(w) for w in windows(values, size)]


def rolling_max(values: List[float], size: int) -> List[float]:
    out: List[float] = []
    for i in range(len(values) - size + 1):
        out.append(min(values[i:i + size]))
    return out
