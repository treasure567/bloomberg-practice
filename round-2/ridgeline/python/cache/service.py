from __future__ import annotations

from typing import Optional

from .lru import LRUCache


class CacheService:
    def __init__(self, capacity: int) -> None:
        self._cache = LRUCache(capacity)

    def get(self, key: str) -> Optional[int]:
        return self._cache.get(key)

    def put(self, key: str, value: int) -> None:
        self._cache.put(key, value)
