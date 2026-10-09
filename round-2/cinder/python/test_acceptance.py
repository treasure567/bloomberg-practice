import pytest

from market_data.feed import MarketDataFeed
from market_data.models import Quote
from market_data.store import QuoteStore
from market_data.subscriptions import SubscriptionHub


def test_store_ignores_stale_seq():
    s = QuoteStore()
    s.apply(Quote("AAPL", 110, 111, seq=2))
    s.apply(Quote("AAPL", 100, 101, seq=1))
    assert s.get("AAPL").seq == 2 and s.get("AAPL").bid_cents == 110


def test_unsubscribe_stops_callbacks():
    hub = SubscriptionHub()
    got = []
    token = hub.subscribe("AAPL", lambda q: got.append(q))
    hub.unsubscribe("AAPL", token)
    hub.publish("AAPL", Quote("AAPL", 100, 101, seq=1))
    assert got == []


def test_publish_isolates_subscriber_errors():
    hub = SubscriptionHub()
    got = []
    hub.subscribe("AAPL", lambda q: (_ for _ in ()).throw(RuntimeError("boom")))
    hub.subscribe("AAPL", lambda q: got.append(q.symbol))
    hub.publish("AAPL", Quote("AAPL", 100, 101, seq=1))
    assert got == ["AAPL"]


def test_delta_before_snapshot_raises():
    feed = MarketDataFeed(QuoteStore())
    with pytest.raises(LookupError):
        feed.apply_delta("AAPL", seq=1, bid_cents=100)
