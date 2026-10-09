from backoff import backoff_delays


def test_exponential_growth():
    assert backoff_delays(1, 4, 100) == [1, 2, 4, 8]


def test_capped_at_max():
    assert backoff_delays(1, 5, 5) == [1, 2, 4, 5, 5]


def test_nonunit_base():
    assert backoff_delays(3, 3, 100) == [3, 6, 12]
