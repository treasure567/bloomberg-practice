from __future__ import annotations

from typing import List

from .book import OrderBook
from .errors import ValidationError
from .models import Trade


class MatchingService:
    def __init__(self) -> None:
        self.book = OrderBook()

    def submit(self, order_id: str, side: str, price: int, qty: int) -> List[Trade]:
        if side not in ("buy", "sell"):
            raise ValidationError("side must be 'buy' or 'sell'")
        if price <= 0 or qty <= 0:
            raise ValidationError("price and qty must be positive")
        return self.book.limit(order_id, side, price, qty)

    def cancel(self, order_id: str) -> None:
        self.book.cancel(order_id)
