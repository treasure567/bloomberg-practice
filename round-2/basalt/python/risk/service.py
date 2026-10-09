from __future__ import annotations

from .netting import NettingService
from .positions import PositionBook


class RiskService:
    def __init__(self) -> None:
        self.positions = PositionBook()
        self.netting = NettingService(self.positions)

    def add_trade(self, trade_id: str, counterparty: str, symbol: str, qty: int) -> None:
        self.netting.add_trade(trade_id, counterparty, symbol, qty)

    def net_position(self, counterparty: str, symbol: str) -> int:
        return self.netting.net_position(counterparty, symbol)
