from stats import moving_average, rolling_max


def test_moving_average_basic():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]


def test_moving_average_full_window():
    assert moving_average([2, 4, 6], 3) == [4.0]


def test_rolling_max():
    assert rolling_max([1, 3, 2, 5, 4], 2) == [3, 3, 5, 5]
