from bus.service import MessageBus


def test_wildcard_segment_match():
    b = MessageBus()
    got = []
    b.subscribe("px.*", lambda m: got.append(m))
    b.publish("px.AAPL", "hi")
    assert got == ["hi"]


def test_unsubscribe_stops_delivery():
    b = MessageBus()
    got = []
    token = b.subscribe("px.AAPL", lambda m: got.append(m))
    b.unsubscribe(token)
    b.publish("px.AAPL", "hi")
    assert got == []


def test_raising_subscriber_does_not_block_others():
    b = MessageBus()
    got = []
    b.subscribe("px.AAPL", lambda m: (_ for _ in ()).throw(RuntimeError("boom")))
    b.subscribe("px.AAPL", lambda m: got.append(m))
    b.publish("px.AAPL", "hi")
    assert got == ["hi"]
