from __future__ import annotations

from typing import Dict, Optional

from .models import Quote


class QuoteStore:
    """Latest quote per symbol, keyed by symbol. Updates arrive with a sequence number."""

    def __init__(self) -> None:
        self._quotes: Dict[str, Quote] = {}

    def apply(self, quote: Quote) -> None:
        self._quotes[quote.symbol] = quote

    def get(self, symbol: str) -> Optional[Quote]:
        return self._quotes.get(symbol)
