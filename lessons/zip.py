"""Combining two lists into a dictionary."""

__author__ = "730695813"


# signature line for zip() function
def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Zip() function returns a zipped dict from two input lists."""
    # initial setup
    output_dict: dict[str, int] = dict()

    # return empty list when lists are empty or of unequal length
    if len(str_list) != len(int_list) or len(str_list) == 0 or len(int_list) == 0:
        return output_dict
    
    # iterate iver lists and store in dict
    for i in range(0, len(str_list), 1):
        output_dict[str_list[i]] = int_list[i]

    # return dict
    return output_dict