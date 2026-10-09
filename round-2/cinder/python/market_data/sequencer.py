from __future__ import annotations

from typing import Dict


class Sequencer:
    """Tracks the highest sequence number seen per symbol, to detect gaps and stale updates."""

    def __init__(self) -> None:
        self._last: Dict[str, int] = {}

    def is_newer(self, symbol: str, seq: int) -> bool:
        return seq > self._last.get(symbol, -1)

    def observe(self, symbol: str, seq: int) -> None:
        if seq > self._last.get(symbol, -1):
            self._last[symbol] = seq

    def last_seq(self, symbol: str) -> int:
        return self._last.get(symbol, -1)
