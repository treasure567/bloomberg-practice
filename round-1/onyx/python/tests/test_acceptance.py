from limiter import FixedWindowLimiter


def test_blocks_after_limit():
    lim = FixedWindowLimiter(2, 10)
    assert [lim.allow(0), lim.allow(1), lim.allow(2)] == [True, True, False]


def test_resets_next_window():
    lim = FixedWindowLimiter(2, 10)
    assert [lim.allow(0), lim.allow(1), lim.allow(2), lim.allow(10)] == [True, True, False, True]
