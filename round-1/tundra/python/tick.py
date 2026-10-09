from __future__ import annotations

from rounding import nearest_multiple


def round_to_tick(price_cents: int, tick_cents: int) -> int:
    return nearest_multiple(price_cents, tick_cents)
