from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Resting:
    order_id: str
    side: str
    price: int
    qty: int
    seq: int


@dataclass(frozen=True)
class Trade:
    maker_id: str
    taker_id: str
    price: int
    qty: int
