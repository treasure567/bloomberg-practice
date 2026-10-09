from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Trade:
    trade_id: str
    counterparty: str
    symbol: str
    qty: int        # signed: positive bought, negative sold
