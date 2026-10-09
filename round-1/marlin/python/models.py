from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Position:
    quantity: int = 0
    cost_basis_cents: int = 0
    last_price_cents: int = 0


class SettlementError(ValueError):
    pass
