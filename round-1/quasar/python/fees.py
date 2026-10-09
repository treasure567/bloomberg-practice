from __future__ import annotations

from tiers import MIN_FEE_CENTS, rate_for


def fee_for(amount_cents: int) -> int:
    return int(amount_cents * rate_for(amount_cents))
