from risk.service import RiskService


def test_signed_netting():
    s = RiskService()
    s.add_trade("t1", "cpA", "X", 10)
    s.add_trade("t2", "cpA", "X", -4)
    assert s.net_position("cpA", "X") == 6


def test_idempotent_on_trade_id():
    s = RiskService()
    s.add_trade("t1", "cpA", "X", 10)
    s.add_trade("t1", "cpA", "X", 10)
    assert s.net_position("cpA", "X") == 10


def test_counterparties_isolated():
    s = RiskService()
    s.add_trade("t1", "cpA", "X", 10)
    s.add_trade("t2", "cpB", "X", 5)
    assert s.net_position("cpA", "X") == 10
    assert s.net_position("cpB", "X") == 5
