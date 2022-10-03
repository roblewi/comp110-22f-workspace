"""Test for utils exercise."""
__author__ = "730571332"


from exercises.ex05.utils import only_evens, concat, sub


"""Testing only_evens."""


def test_only_evens_empty() -> None:
    """Testing only_evens with an empty list."""
    xs = []
    assert only_evens(xs) == []


def test_only_evens_only_odds() -> None:
    """Testing only_evens with a list of only odds."""
    xs = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_only_evens() -> None:
    """Testing only_evens with a list of only_evens."""
    xs = [2, 4, 6, 8, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


"""Testing concat."""


def test_concat_both_empty() -> None:
    """Testing concat with an empty list."""
    xs = []
    ys = []
    assert concat(xs, ys) == []


def test_concat_second_empty() -> None:
    """Testing concat with the second list being empty."""
    xs = [1, 2, 3, 4]
    ys = []
    assert concat(xs, ys) == [1, 2, 3, 4]


def test_concat_first_empty() -> None:
    """Testing concat with the first list being empty."""
    xs = []
    ys = [1, 2, 3, 4]
    assert concat(xs, ys) == [1, 2, 3, 4]


"""Testing sub."""


def test_sub_empty() -> None:
    """Testing sub with an empty list."""
    xs = []
    start_index = 0
    end_index = 0
    assert sub(xs, start_index, end_index) == []


def test_sub_length_one() -> None:
    """Testing sub with a negative start_index value."""
    xs = ["one"]
    start_index = -10
    end_index = 3
    assert sub(xs, start_index, end_index) == ["one"]


def test_sub_end_out_of_range() -> None:
    """Testing sub with an out-of-range end_index."""
    xs = ["one", "two"]
    start_index = 0
    end_index = 4
    assert sub(xs, start_index, end_index) == ["one", "two"]