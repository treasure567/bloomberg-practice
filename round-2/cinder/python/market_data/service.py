from __future__ import annotations

from .feed import MarketDataFeed
from .models import Quote
from .store import QuoteStore
from .subscriptions import Callback, SubscriptionHub


class MarketDataService:
    def __init__(self) -> None:
        self.store = QuoteStore()
        self.hub = SubscriptionHub()
        self.feed = MarketDataFeed(self.store)

    def subscribe(self, symbol: str, callback: Callback) -> int:
        return self.hub.subscribe(symbol, callback)

    def unsubscribe(self, symbol: str, token: int) -> None:
        self.hub.unsubscribe(symbol, token)

    def on_snapshot(self, quote: Quote) -> None:
        self.feed.apply_snapshot(quote)
        latest = self.store.get(quote.symbol)
        if latest is not None:
            self.hub.publish(quote.symbol, latest)
