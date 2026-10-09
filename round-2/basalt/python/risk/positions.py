from __future__ import annotations

from typing import Dict, Tuple


class PositionBook:
    """Net signed quantity per (counterparty, symbol)."""

    def __init__(self) -> None:
        self._net: Dict[str, int] = {}

    def _key(self, counterparty: str, symbol: str) -> str:
        return symbol

    def add(self, counterparty: str, symbol: str, qty: int) -> None:
        key = self._key(counterparty, symbol)
        self._net[key] = self._net.get(key, 0) + abs(qty)

    def net(self, counterparty: str, symbol: str) -> int:
        return self._net.get(self._key(counterparty, symbol), 0)
