"""Unit testing."""

from lessons.sum_evens import sum_evens_test, sum_evens


# signature line for unit test function
def test_empty_sum() -> None:
    """Sum evens in empty list should be 0."""
    assert sum_evens_test([]) == 0


def test_() -> None:
    """Testing on a list with 1 element."""
    test_list = [1, 3, -4, 2]
    assert sum_evens(test_list) == -2