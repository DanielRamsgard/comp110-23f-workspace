"""Practice summing over lists."""


# signature line for sum_evens() function
def sum_evens_test(input_list: list[int]) -> int:
    """Sum only evens."""
    # initial setup
    sum: int = 0
    return sum


# signature line for sum_evens() function
def sum_evens(input_list: list[int]) -> int:
    """Sum only evens."""
    # initial setup
    sum: int = 0

    # add evens
    for i in range(0, len(input_list), 1):
        if input_list[i] % 2 == 0:
            sum += input_list[i]

    # return sum
    return sum