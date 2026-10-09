from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from models import Position, SettlementError


@dataclass
class Blotter:
    positions: Dict[str, Position] = field(default_factory=dict)
    realized_pnl_cents: int = 0
    _seen: set = field(default_factory=set)

    def apply(self, fill: dict) -> None:
        trade_id = fill["trade_id"]
        symbol = fill["symbol"]
        side = fill["side"]
        qty = fill["quantity"]
        price = fill["price_cents"]
        pos = self.positions.setdefault(symbol, Position())
        if side == "buy":
            pos.quantity += qty
            pos.cost_basis_cents += qty * price
            pos.last_price_cents = price
        else:
            avg = pos.cost_basis_cents / pos.quantity
            self.realized_pnl_cents += (price - pos.last_price_cents) * qty
            pos.quantity -= qty
            pos.cost_basis_cents -= int(avg * qty)


def settle(fills: List[dict]) -> Blotter:
    b = Blotter()
    for f in fills:
        b.apply(f)
    return b
