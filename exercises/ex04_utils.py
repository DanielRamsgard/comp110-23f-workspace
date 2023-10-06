"""Creating new functions and operations with lists."""
__author__ = "730695813"


def all(input_list: list[int], num: int) -> bool:
    if len(input_list) == 0:
        return False
    i: int = 0
    while (i < len(input_list)):
        if input_list[i] != num:
            return False
        i += 1
    return True


def max(input_list: list[int]) -> int:
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    current_int: int = 0
    while (i < len(input_list)):
        if current_int < input_list[i]:
            current_int = input_list[i]
        i += 1 
    largest_int = current_int
    return largest_int


def is_equal(input_list_1: list[int], input_list_2: list[int]) -> bool:
    if len(input_list_1) == 0 and len(input_list_2) == 0:
        raise ValueError("both is_equal() arguments are empty lists")
    elif len(input_list_1) == 0 or len(input_list_2) == 0:
        raise ValueError("an is_equal() arg is an empty list")
    if len(input_list_1) != len(input_list_2):
        print("is_equal arguments are not equal in length")
        return
    i: int = 0
    while (i < len(input_list_1)):
        if input_list_1[i] != input_list_2[i]:
            return False
        i += 1
    return True

