from __future__ import annotations

from typing import Dict


class Inventory:
    """Physical on-hand counts per SKU (does not account for reservations)."""

    def __init__(self, stock: Dict[str, int] | None = None) -> None:
        self._on_hand: Dict[str, int] = dict(stock or {})

    def set_stock(self, sku: str, qty: int) -> None:
        self._on_hand[sku] = qty

    def on_hand(self, sku: str) -> int:
        return self._on_hand.get(sku, 0)
