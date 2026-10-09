from split import split_amount


def test_split_100_3():
    assert split_amount(100, 3) == [34, 33, 33]


def test_split_10_4():
    assert split_amount(10, 4) == [3, 3, 2, 2]


def test_split_7_2():
    assert split_amount(7, 2) == [4, 3]
