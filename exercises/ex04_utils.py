"""Creating new functions and operations with lists."""
__author__ = "730695813"


def all(input_list: list[int], num: int) -> bool:
    """This function if a given input integer is inside of an input list."""
    if len(input_list) == 0:
        return False
    i: int = 0
    while (i < len(input_list)):
        if input_list[i] != num:
            return False
        i += 1
    return True


def max(input_list: list[int]) -> int:
    """This function takes a list as input and returns the largest value."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 1
    current_int: int = input_list[0]
    while (i < len(input_list)):
        if current_int < input_list[i]:
            current_int = input_list[i]
        i += 1 
    largest_int = current_int
    return largest_int


def is_equal(input_list_1: list[int], input_list_2: list[int]) -> bool:
    """This function checks to see whether or not every value at every index of each of these lists are equal."""
    if len(input_list_1) == 0 and len(input_list_2) == 0:
        return True
    elif len(input_list_1) == 0 or len(input_list_2) == 0:
        return False
    if len(input_list_1) != len(input_list_2):
        return False
    i: int = 0
    while (i < len(input_list_1)):
        if input_list_1[i] != input_list_2[i]:
            return False
        i += 1
    return True