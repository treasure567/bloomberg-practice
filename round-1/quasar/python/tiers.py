from __future__ import annotations

MIN_FEE_CENTS = 50


def rate_for(amount_cents: int) -> float:
    if amount_cents <= 10000:
        return 0.02
    if amount_cents <= 100000:
        return 0.01
    return 0.005
