from matching.service import MatchingService


def test_price_time_priority_fifo():
    s = MatchingService()
    s.submit("A", "sell", 100, 5)
    s.submit("B", "sell", 100, 5)
    trades = s.submit("T", "buy", 100, 5)
    assert len(trades) == 1
    assert trades[0].maker_id == "A"


def test_partial_fill_reduces_resting_qty():
    s = MatchingService()
    s.submit("A", "sell", 100, 10)
    first = s.submit("T1", "buy", 100, 4)
    assert len(first) == 1 and first[0].qty == 4
    second = s.submit("T2", "buy", 100, 6)
    assert len(second) == 1 and second[0].qty == 6


def test_cancel_removes_resting_order():
    s = MatchingService()
    s.submit("A", "sell", 100, 5)
    s.cancel("A")
    assert s.submit("T", "buy", 100, 5) == []
