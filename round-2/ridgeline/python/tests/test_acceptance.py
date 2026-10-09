from cache.service import CacheService


def test_evicts_least_recently_used():
    c = CacheService(2)
    c.put("a", 1); c.put("b", 2); c.put("c", 3)
    assert c.get("a") is None
    assert c.get("b") == 2
    assert c.get("c") == 3


def test_get_refreshes_recency():
    c = CacheService(2)
    c.put("a", 1); c.put("b", 2)
    c.get("a")
    c.put("c", 3)
    assert c.get("a") == 1
    assert c.get("b") is None


def test_update_existing_refreshes_without_growth():
    c = CacheService(2)
    c.put("a", 1); c.put("b", 2)
    c.put("a", 9)
    c.put("c", 3)
    assert c.get("a") == 9
    assert c.get("b") is None
