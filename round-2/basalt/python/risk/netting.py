from __future__ import annotations

from .positions import PositionBook


class NettingService:
    def __init__(self, positions: PositionBook) -> None:
        self.positions = positions
        self._seen: set = set()

    def add_trade(self, trade_id: str, counterparty: str, symbol: str, qty: int) -> None:
        self.positions.add(counterparty, symbol, qty)

    def net_position(self, counterparty: str, symbol: str) -> int:
        return self.positions.net(counterparty, symbol)
