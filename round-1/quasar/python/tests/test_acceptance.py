from fees import fee_for


def test_min_fee_floor():
    assert fee_for(2000) == 50


def test_boundary_10000_is_one_percent():
    assert fee_for(10000) == 100


def test_boundary_100000_is_half_percent():
    assert fee_for(100000) == 500
