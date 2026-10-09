from __future__ import annotations

from typing import Dict

from .models import Reservation


class ReservationBook:
    def __init__(self) -> None:
        self._reservations: Dict[str, Reservation] = {}

    def place(self, reservation_id: str, sku: str, qty: int) -> None:
        self._reservations[reservation_id] = Reservation(reservation_id, sku, qty, active=True)

    def release(self, reservation_id: str) -> None:
        pass

    def has(self, reservation_id: str) -> bool:
        return reservation_id in self._reservations

    def reserved(self, sku: str) -> int:
        return sum(r.qty for r in self._reservations.values() if r.active and r.sku == sku)
