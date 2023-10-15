"""Creating new functions and operations with lists."""
__author__ = "730695813"


# signature line for all() function
def all(input_list: list[int], num: int) -> bool:
    """This function if a given input integer is inside of an input list."""
    # checks to see if input list is empty
    if len(input_list) == 0:
        return False
    i: int = 0
    # iterates over list to check if any values do not equal input integer
    while (i < len(input_list)):
        if input_list[i] != num:
            return False
        i += 1
    return True


# singature line for max() function
def max(input_list: list[int]) -> int:
    """This function takes a list as input and returns the largest value."""
    # returns error if the input list is empty
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 1
    current_largest_int: int = input_list[0]
    # iterates over the list setting the largest integer for two subsequent elements
    while (i < len(input_list)):
        if current_largest_int < input_list[i]:
            current_largest_int = input_list[i]
        i += 1 
        # sets new final largest_int value for clarity
    largest_int = current_largest_int
    return largest_int


# signature line for is_equal() function
def is_equal(input_list_1: list[int], input_list_2: list[int]) -> bool:
    """This function checks to see whether or not every value at every index of each of these lists are equal."""
    # checks to see whether both lists are empty or not
    if len(input_list_1) == 0 and len(input_list_2) == 0:
        return True
    # checks to see if either list is empty
    elif len(input_list_1) == 0 or len(input_list_2) == 0:
        return False
    # checks to see if the length of both lists match
    if len(input_list_1) != len(input_list_2):
        return False
    i: int = 0
    # iterates over the two lists to see if elements at the same indexs are not equal
    while (i < len(input_list_1)):
        if input_list_1[i] != input_list_2[i]:
            return False
        i += 1
    return True