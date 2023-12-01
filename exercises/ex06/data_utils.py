"""Dictionary related utility functions."""
from csv import DictReader

__author__ = "730695813"


# Define your functions below
def read_csv_rows(filepath: str) -> list[dict[str, str]]:
    """Reads csv rows and returns said rows."""
    # initial setup
    final_list: list[dict[str, str]] = list()
    file_handle = open(filepath, "r", encoding="utf8")
    rows = DictReader(file_handle)

    # iterate over data
    for row in rows:
        final_list.append(row)

    # return row and close file
    file_handle.close()
    return final_list


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Returns alll values within a given column."""
    # initial setup
    final_list: list[str] = list()

    # iterate over list
    for row in table:
        final_list.append(row[key])

    # return list
    return final_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms table."""
    # initial setup
    new_dict: dict[str, list[str]] = dict()

    # initialize lists
    for row in table:
        for key in row:
            new_dict[key] = list()

    # store columns
    for row in table:
        for key in row:
            new_dict[key].append(row[key])

    # return dict
    return new_dict


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Returns a head of the entire table."""
    # initial setup
    new_dict: dict[str, list[str]] = dict()

    # iterate over 
    for column in table:
        new_dict[column] = list()
        for i in range(0, N, 1):
            new_dict[column].append(table[column][i])

    # return new dict
    return new_dict


def select(table: dict[str, list[str]], input_list: list[str]) -> dict[str, list[str]]:
    """Produce new table with specific subset of columns."""
    # initial setup
    new_dict: dict[str, list[str]] = dict()
    
    # iterate over table
    for key in table:
        for val in input_list:
            if key == val:
                new_dict[key] = table[key]

    # return dict
    return new_dict


def concat(table_0: dict[str, list[str]], table_1: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenates two tables."""
    new_table: dict[str, list[str]] = dict()

    for key in table_0:
        new_table[key] = table_0[key]

    for key in table_1:
        new_table[key] = table_1[key]

    return new_table


def count(input_list: list[str]) -> dict[str, int]:
    """Returns the count of each element in input list."""
    # initial setup
    final_dict: dict[str, int] = dict()
    i: int = 0

    # iterate over input list
    for val in input_list:
        for key in input_list:
            if val == key:
                i += 1

        final_dict[val] = i
        i = 0

    # return dict
    return final_dict