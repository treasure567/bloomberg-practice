from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Sku:
    sku: str
    description: str


@dataclass
class Reservation:
    reservation_id: str
    sku: str
    qty: int
    active: bool = True
