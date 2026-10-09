from __future__ import annotations

from typing import List

from ordering import by_start


def merge(intervals: List[List[int]]) -> List[List[int]]:
    ordered = by_start(intervals)
    if not ordered:
        return []
    merged = [list(ordered[0])]
    for s, e in ordered[1:]:
        last = merged[-1]
        if s < last[1]:
            last[1] = max(last[1], e)
        else:
            merged.append([s, e])
    return merged
