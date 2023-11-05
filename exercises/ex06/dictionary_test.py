"""Exercise to test dictionary exercise."""

from dictionary import invert, favorite_color, count, alphabetizer, update_attendance

__author__ = "730695813"


# signature line for use case one of invert() function
def test_invert_use_case_1() -> None:
    """Swaps key-value pairs with one key-value pair as input."""
    # initial setup
    test_dict: dict[str, str] = {"apples": "5"}
    final_dict: dict[str, str] = {"5": "apples"}

    # assert statement for unit testing
    assert invert(test_dict) == final_dict


# signature line for use case two of invert() function
def test_invert_use_case_2() -> None:
    """Swaps correctly key-value pairs when there are two input keys-value pairs."""
    # initial setup
    test_dict: dict[str, str] = {"apple": "1", "banana": "2"}
    final_dct: dict[str, str] = {"1": "apple", "2": "banana"}

    # assert statement for unit testing
    assert invert(test_dict) == final_dct


# signature line for an edge case of invert() function
def test_invert_edge_case() -> None:
    """Returns an empty dict if an the input is an empty dict."""
    # initial setup
    test_dict: dict[str, str] = dict()
    final_dict: dict[str, str] = dict()

    # assert statement for unit testing
    assert invert(test_dict) == final_dict


# siganture line for use case one of favorite_color() function
def test_favorite_color_use_case_1() -> None:
    """Returns the most popular color in a dictionary."""
    # initial setup
    test_dict: dict[str, str] = {"Billy": "blue", "Bobby": "red", "Randy": "blue"}
    final_str: str = "blue"

    # assert statement for unit testing
    assert favorite_color(test_dict) == final_str


# signature line for use case two of favorite_color() function
def test_favorite_color_use_case_2() -> None:
    """Returns the first value if there is a tie in the favorite color counts."""
    # initial setup
    test_dict: dict[str, str] = {"Billy": "blue", "Bobby": "red", "Randy": "green"}
    final_str: str = "blue"

    # assert statement for unit testing
    assert favorite_color(test_dict) == final_str


# signature line for an edge case of favorite_color() function
def test_favorite_color_edge_case() -> None:
    """Returns 'None' if the input is an empty dict."""
    # initial setup
    test_dict: dict[str, str] = dict()
    final_str: str = "None"

    # assert statement for unit testing
    assert favorite_color(test_dict) == final_str


# signature line for use case one of count() function
def test_count_use_case_1() -> None:
    """Returns a dict with keys and counts of 1 (because list had all unique elements)."""
    # initial setup
    test_list: list[str] = ["Bobby", "Jared", "Simon", "Cader"]
    final_dict: dict[str, int] = {"Bobby": 1, "Jared": 1, "Simon": 1, "Cader": 1}

    # assert statement for unit testing
    assert count(test_list) == final_dict


# signature line for use case two of count() function
def test_count_use_case_2() -> None:
    """Returns a dict with keys and counts of 1 or more with repeat list input elements."""
    # initial setup
    test_list: list[str] = ["Bobby", "Bobby", "Simon", "Simon"]
    final_dict: dict[str, int] = {"Bobby": 2, "Simon": 2}

    # assert statement for unit testing
    assert count(test_list) == final_dict


# signature line for an edge case of count() function
def test_count_edge_case() -> None:
    """Returns an empty dict from an input of an empty dict."""
    # initaial setup
    test_list: list[str] = list()
    final_dict: dict[str, int] = dict()

    # assert statement for unit testing
    assert count(test_list) == final_dict


# signature line for use case one of alphabetizer() function
def test_alphabetizer_use_case_1() -> None:
    """Returns only one key bacause each input str begins with the same letter."""
    # initial setup
    test_list: list[str] = ["bobby", "benny", "billy", "big ben"]
    final_dict: dict[str, list[str]] = {"b": ["bobby", "benny", "billy", "big ben"]}

    # assert statement for unit testing
    assert alphabetizer(test_list) == final_dict


# signature line for use case two of alphabetizer() function
def test_alphabetizer_use_case_2() -> None:
    """Returns multiple keys as elements began with different letters at least once in the input list."""
    # initial setup
    test_list: list[str] = ["cader", "dan", "wyatt", "william"]
    final_dict: dict[str, list[str]] = {"c": ["cader"], "d": ["dan"], "w": ["wyatt", "william"]}

    # assert statement for unit testing
    assert alphabetizer(test_list) == final_dict


# signature line for an edge case of alphabetizer() function
def test_alphabetizer_edge_case() -> None:
    """Returns an empty dict given an empty input list."""
    # initial setup
    test_list: list[str] = list()
    final_dict: dict[str, list[str]] = dict()

    # assert statement for unit testing
    assert alphabetizer(test_list) == final_dict


# signature line for use case one of update_attendance() function
def test_update_attendance_use_case_1() -> None:
    """Creates a new day and new student attendance on that day."""
    # initial setup
    test_dict: dict[str, list[str]] = {}
    test_day: str = "Tuesday"
    test_student: str = "Billy"
    final_dict: dict[str, list[str]] = {"Tuesday": ["Billy"]}

    # assert statement for unit testing
    assert update_attendance(test_dict, test_day, test_student) == final_dict


# signature line for use case two of update_attendance() functon
def test_update_attendance_use_case_2() -> None:
    """Appends new student to existing day."""
    # initial setup
    test_dict: dict[str, list[str]] = {"Tuesday": ["Bobby"]}
    test_day: str = "Tuesday"
    test_student: str = "Billy"
    final_dict: dict[str, list[str]] = {"Tuesday": ["Bobby", "Billy"]}

    # assert statement for unit tesing
    assert update_attendance(test_dict, test_day, test_student) == final_dict


# signature line for an edge case of update_attendance() function
def test_update_attendance_edge_case() -> None:
    """Returns an empty dict from an input empty dict."""
    # initial setup
    test_dict: dict[str, list[str]] = dict()
    test_day: str = ""
    test_student: str = ""
    final_dict: dict[str, list[str]] = dict()

    # assert statement for unit tesing
    assert update_attendance(test_dict, test_day, test_student) == final_dict