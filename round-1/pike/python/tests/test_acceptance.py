from intervals import merge


def test_merge_unsorted_overlaps():
    assert merge([[1, 3], [2, 4], [8, 10], [4, 6]]) == [[1, 6], [8, 10]]


def test_touching_intervals_merge():
    assert merge([[1, 2], [2, 3]]) == [[1, 3]]


def test_output_sorted():
    assert merge([[5, 6], [1, 2]]) == [[1, 2], [5, 6]]
