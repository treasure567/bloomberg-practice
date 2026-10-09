import pytest

from fulfillment.catalog import Catalog
from fulfillment.errors import OutOfStock
from fulfillment.inventory import Inventory
from fulfillment.reservations import ReservationBook
from fulfillment.service import FulfillmentService


def svc():
    cat = Catalog(); cat.add("A", "widget")
    inv = Inventory({"A": 10})
    return FulfillmentService(cat, inv, ReservationBook())


def test_available_reflects_reservations():
    s = svc()
    s.reserve("r1", "A", 3)
    assert s.available("A") == 7


def test_oversell_rejected():
    s = svc()
    with pytest.raises(OutOfStock):
        s.reserve("r2", "A", 100)


def test_release_restores_availability():
    s = svc()
    s.reserve("r1", "A", 3)
    assert s.available("A") == 7
    s.release("r1")
    assert s.reserved("A") == 0
    assert s.available("A") == 10
