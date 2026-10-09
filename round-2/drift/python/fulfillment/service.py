from __future__ import annotations

from .catalog import Catalog
from .errors import OutOfStock, ValidationError
from .inventory import Inventory
from .reservations import ReservationBook


class FulfillmentService:
    def __init__(self, catalog: Catalog, inventory: Inventory, reservations: ReservationBook) -> None:
        self.catalog = catalog
        self.inventory = inventory
        self.reservations = reservations

    def available(self, sku: str) -> int:
        return self.inventory.on_hand(sku)

    def reserve(self, reservation_id: str, sku: str, qty: int) -> None:
        if qty <= 0:
            raise ValidationError("qty must be positive")
        self.catalog.require(sku)
        self.reservations.place(reservation_id, sku, qty)

    def release(self, reservation_id: str) -> None:
        self.reservations.release(reservation_id)

    def reserved(self, sku: str) -> int:
        return self.reservations.reserved(sku)
