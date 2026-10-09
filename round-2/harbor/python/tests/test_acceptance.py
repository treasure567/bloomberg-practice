import pytest

from payments.errors import InsufficientFunds
from payments.service import PaymentsService


def svc():
    s = PaymentsService()
    s.open_account("A")
    s.open_account("B")
    return s


def test_transfer_moves_funds():
    s = svc()
    s.deposit("A", 100)
    s.transfer("t1", "A", "B", 40)
    assert s.balance("A") == 60
    assert s.balance("B") == 40


def test_transfer_is_idempotent():
    s = svc()
    s.deposit("A", 100)
    s.transfer("t1", "A", "B", 40)
    s.transfer("t1", "A", "B", 40)
    assert s.balance("B") == 40


def test_overdraft_considering_holds_rejected():
    s = svc()
    s.deposit("A", 100)
    s.place_hold("h1", "A", 40)          # available is now 60
    with pytest.raises(InsufficientFunds):
        s.transfer("t1", "A", "B", 80)


def test_release_restores_available():
    s = svc()
    s.deposit("A", 100)
    s.place_hold("h1", "A", 30)
    assert s.available("A") == 70
    s.release_hold("h1")
    assert s.available("A") == 100


def test_double_entry_conservation():
    s = svc()
    s.deposit("A", 100)
    s.transfer("t1", "A", "B", 40)
    assert sum(s.balances().values()) == 0
