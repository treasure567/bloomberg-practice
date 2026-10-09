from __future__ import annotations

from .models import Quote
from .store import QuoteStore


class MarketDataFeed:
    def __init__(self, store: QuoteStore) -> None:
        self.store = store

    def apply_snapshot(self, quote: Quote) -> None:
        self.store.apply(quote)

    def apply_delta(self, symbol: str, seq: int, bid_cents: int | None = None,
                    ask_cents: int | None = None) -> None:
        current = self.store.get(symbol)
        bid = bid_cents if bid_cents is not None else (current.bid_cents if current else 0)
        ask = ask_cents if ask_cents is not None else (current.ask_cents if current else 0)
        self.store.apply(Quote(symbol, bid, ask, seq))
