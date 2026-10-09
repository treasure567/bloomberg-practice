from sessions.service import SessionService


def test_expiry_boundary_is_inclusive():
    s = SessionService()
    s.create("s", now=0, ttl=10)
    assert s.get("s", 10) is None


def test_touch_refreshes_expiry():
    s = SessionService()
    s.create("s", now=0, ttl=10)
    s.touch("s", 8, 10)
    assert s.get("s", 15) is not None


def test_cleanup_removes_expired():
    s = SessionService()
    s.create("s", now=0, ttl=10)
    s.cleanup(10)
    assert s.get("s", 10) is None
    assert s.size() == 0
