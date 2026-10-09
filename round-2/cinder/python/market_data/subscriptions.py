from __future__ import annotations

import itertools
from typing import Callable, Dict, List, Tuple

from .models import Quote

Callback = Callable[[Quote], None]


class SubscriptionHub:
    def __init__(self) -> None:
        self._subs: Dict[str, List[Tuple[int, Callback]]] = {}
        self._counter = itertools.count(1)

    def subscribe(self, symbol: str, callback: Callback) -> int:
        token = next(self._counter)
        self._subs.setdefault(symbol, []).append((token, callback))
        return token

    def unsubscribe(self, symbol: str, token: int) -> None:
        subs = self._subs.get(symbol, [])
        self._subs[symbol] = [(t, cb) for (t, cb) in subs if cb != token]

    def publish(self, symbol: str, quote: Quote) -> None:
        for (_, callback) in self._subs.get(symbol, []):
            callback(quote)
