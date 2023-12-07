"""Function writing for final."""


def free_biscuits(input_dict: dict[str, list[int]]) -> dict[str, bool]:
    """Gets some free stuff if points is greater than 100."""
    # initial setup
    new_dict: dict[str, bool] = dict()
    sum: int = 0

    # loop over keys
    for key in input_dict:
        for val in input_dict[key]:
            sum += val
        if sum >= 100:
            new_dict[key] = True
        else: 
            new_dict[key] = False
        sum = 0
        
    return new_dict


def max_key(input_dict: dict[str, list[int]]) -> str:
    """Returns key with greatest sum."""
    max_key: str = "" 
    max_sum: int = 0
    sum: int = 0

    for key in input_dict:
        for val in input_dict[key]:
            sum += val
        if sum > max_sum:
            max_sum = sum
        sum = 0

    for key in input_dict:
        for val in input_dict[key]:
            sum += val
        if sum == max_sum:
            return key
        sum = 0


def multiples(input_list: list[int]) -> list[bool]:
    """Previoud val multiple or not."""
    # initial setup
    final_list: list[bool] = list()

    # loop over list
    for i in range(0, len(input_list), 1):
        if i == 0:
            if input_list[i] % input_list[-1] == 0:
                final_list.append(True)
            else:
                final_list.append(False)
        else:
            if input_list[i] % input_list[i-1] == 0:
                final_list.append(True)
            else:
                final_list.append(False)
    
    return final_list


def merge_lists(list_first: list[str], list_second: list[int]) -> dict[str, int]:
    """Creates a hash map that connects input lists."""
    # initial setup
    new_dict: dict[str, int] = dict()
    if len(list_first) != len(list_second):
        return new_dict

    for i in range(len(list_first)):
        new_dict[list_first[i]] = list_second[i]

    # return dict
    return new_dict


def reverse_multiply(input_list: list[int]) -> list[int]:
    """Performs reverse mul."""
    new_list: list[int] = list()
    i: int = len(input_list) - 1

    while i >= 0:
        new_list.append(input_list[i] * 2)
        i -= 1

    return new_list