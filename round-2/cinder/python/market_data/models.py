from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Quote:
    symbol: str
    bid_cents: int
    ask_cents: int
    seq: int        # monotonically increasing per symbol; higher is newer
