from __future__ import annotations

import itertools
from typing import List

from .models import Callback, Subscription


class SubscriptionRegistry:
    def __init__(self) -> None:
        self._subs: List[Subscription] = []
        self._counter = itertools.count(1)

    def add(self, pattern: str, callback: Callback) -> int:
        token = next(self._counter)
        self._subs.append(Subscription(token, pattern, callback))
        return token

    def remove(self, token: int) -> None:
        self._subs = [s for s in self._subs if s.pattern != token]

    def all(self) -> List[Subscription]:
        return list(self._subs)
