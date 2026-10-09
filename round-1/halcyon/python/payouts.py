from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List

POT_SEED_CENTS = 10_000_00
ENTRY_FEE_CENTS = 5_00
TIER_PERCENT = {5: 100, 4: 40, 3: 20, 2: 5}


@dataclass
class Payout:
    participant: str
    match_count: int
    amount_cents: int


@dataclass
class DrawResult:
    pot_cents: int
    payouts: List[Payout] = field(default_factory=list)
    rollover_cents: int = 0


def pot_cents(entry_count: int) -> int:
    return POT_SEED_CENTS + ENTRY_FEE_CENTS * entry_count


def distribute(entries, winning_code: str, matcher: Callable[[str, str], int]) -> DrawResult:
    pot = pot_cents(len(entries))
    by_tier: Dict[int, List] = {}
    for e in entries:
        m = matcher(e.code, winning_code)
        if m >= 2:
            by_tier.setdefault(m, []).append(e)
    payouts: List[Payout] = []
    awarded = 0
    for tier in (2, 3, 4, 5):
        winners = by_tier.get(tier, [])
        if not winners:
            continue
        amount = pot * TIER_PERCENT[tier] // 100
        share = amount / len(winners)
        for w in winners:
            payouts.append(Payout(w.participant, tier, int(share)))
            awarded += int(share)
    return DrawResult(pot, payouts, pot - awarded)
