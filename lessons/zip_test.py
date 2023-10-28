"""Test my zip function."""

from lessons.zip import zip

__author__ = "730695813"


# signature line for use case one
def test_use_case_1() -> None:
    """Properly zips corrcet indexs with different first list strings."""
    # initial setup
    input_list_1: list[str] = ["Tuesday", "Monday"]
    input_list_2: list[int] = [1, 2]
    final_dict: dict[str, int] = {"Tuesday": 1, "Monday": 2}

    # assertation
    assert zip(input_list_1, input_list_2) == final_dict


# signature line for use case two
def test_use_case_2() -> None:
    """Properly zips corrcet indexs with same first list strings with only length of 1 lists."""
    # initial setup
    input_list_1: list[str] = ["Tuesday"]
    input_list_2: list[int] = [1]
    final_dict: dict[str, int] = {"Tuesday": 1}

    # assertation
    assert zip(input_list_1, input_list_2) == final_dict


# signature line for edge case one
def test_edge_case_1() -> None:
    """Returns an empty dict from inputs of empty list(s)."""
    # initial setup
    input_list_1: list[str] = ["Tuesday"]
    input_list_2: list[int] = list()
    final_dict: dict[str, int] = dict()

    # assertation
    assert zip(input_list_1, input_list_2) == final_dict