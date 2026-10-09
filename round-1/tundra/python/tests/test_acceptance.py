from tick import round_to_tick


def test_rounds_up_near_tick():
    assert round_to_tick(103, 5) == 105


def test_rounds_to_nearest():
    assert round_to_tick(108, 5) == 110


def test_tie_rounds_up():
    assert round_to_tick(1025, 50) == 1050
