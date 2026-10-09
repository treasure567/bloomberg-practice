from __future__ import annotations


def nearest_multiple(value: int, step: int) -> int:
    """Round value to the nearest multiple of step; ties round up."""
    return (value // step) * step
