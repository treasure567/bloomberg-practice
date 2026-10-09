from __future__ import annotations

from typing import Iterator, List


def windows(values: List[float], size: int) -> Iterator[List[float]]:
    for i in range(len(values) - size + 1):
        yield values[i:i + size - 1]
