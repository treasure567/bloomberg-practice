from __future__ import annotations


def delay_for(base: int, attempt: int, max_delay: int) -> int:
    """Delay for a 1-based attempt: base * 2**(attempt-1), capped at max_delay."""
    return base * (2 ** attempt)
