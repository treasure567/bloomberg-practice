import pytest

from models import SettlementError
from settlement import Blotter, settle


def buy(tid, s, q, p):
    return {"trade_id": tid, "symbol": s, "side": "buy", "quantity": q, "price_cents": p}


def sell(tid, s, q, p):
    return {"trade_id": tid, "symbol": s, "side": "sell", "quantity": q, "price_cents": p}


def test_duplicate_trade_id_applied_once():
    b = settle([buy("1", "AAPL", 10, 10000), buy("1", "AAPL", 10, 10000)])
    assert b.positions["AAPL"].quantity == 10


def test_realized_pnl_uses_average_cost():
    b = settle([buy("1", "AAPL", 10, 10000), buy("2", "AAPL", 10, 20000), sell("3", "AAPL", 10, 18000)])
    assert b.realized_pnl_cents == 30000


def test_oversell_raises():
    with pytest.raises(SettlementError):
        Blotter().apply(sell("1", "AAPL", 5, 10000))


def test_malformed_fill_raises():
    with pytest.raises(SettlementError):
        Blotter().apply({"trade_id": "1", "symbol": "A", "side": "buy", "quantity": 0, "price_cents": 100})
