"""Summing the elements of a list using different loops."""

__author__ = "730695813"

vals: list[float] = [1.1, 0.9, 1.0]


# signature line for w_sum() function
def w_sum(vals: list[float]) -> float:
    """Function tht takes inputs and computes a sum, using a while loop."""
    i: int = 0
    sum: float = 0.0

    while (i < len(vals)):
        sum += vals[i]
        i += 1
    
    return sum


# signature line for f_sum() function
def f_sum(vals: list[float]) -> float:
    """Function that takes inputs and computes a sum, using a for ... in ... loop."""
    sum: float = 0.0

    for val in vals:
        sum += val

    return sum


# signature line for f_sum_range() function
def f_range_sum(vals: list[float]) -> float:
    """Function that takes inputs and computes a sum, using a for ... in range(len(xs)) loop."""
    sum: float = 0.0

    for i in range(0, len(vals), 1):
        sum += vals[i]
        i += 1

    return sum