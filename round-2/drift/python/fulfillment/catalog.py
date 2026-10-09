from __future__ import annotations

from typing import Dict

from .errors import UnknownSku
from .models import Sku


class Catalog:
    def __init__(self) -> None:
        self._skus: Dict[str, Sku] = {}

    def add(self, sku: str, description: str = "") -> None:
        self._skus[sku] = Sku(sku, description)

    def exists(self, sku: str) -> bool:
        return sku in self._skus

    def require(self, sku: str) -> None:
        if sku not in self._skus:
            raise UnknownSku(sku)
