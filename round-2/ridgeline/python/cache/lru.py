from __future__ import annotations

from collections import OrderedDict
from typing import Optional


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._data: "OrderedDict[str, int]" = OrderedDict()

    def get(self, key: str) -> Optional[int]:
        if key not in self._data:
            return None
        return self._data[key]

    def put(self, key: str, value: int) -> None:
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=True)
