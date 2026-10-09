from __future__ import annotations


def window_of(now: int, size: int) -> int:
    """Index of the fixed window that `now` falls into."""
    return now // size
