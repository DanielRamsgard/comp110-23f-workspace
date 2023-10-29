"""This code is for ex06 dictionary work."""

__author__ = "730695813"


# signature line for invert() function
def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts key-value pairs."""
    # initial setup
    new_key_list: list[str] = list()
    repetition_counter: int = 0
    new_value_list: list[str] = list()
    new_dict: dict[str, str] = dict()
    empty_dict: dict[str, str] = dict()

    # make sure list isn't empty
    if len(input_dict) == 0:
        return empty_dict

    # loop over keys
    for elem in input_dict:
        new_key_list.append(input_dict[elem])

    # check if any are similar
    for i in range(0, len(new_key_list), 1):
        for j in range(0, len(new_key_list), 1):
            if new_key_list[i] == new_key_list[j]:
                repetition_counter += 1
        if repetition_counter >= 2:
            raise KeyError("You cannot have two input values that are equal")
        repetition_counter = 0
    
    # switch keys and values
    for elem in input_dict:
        new_value_list.append(elem)

    # create new dict
    for i in range(0, len(input_dict), 1):
        new_dict[new_key_list[i]] = new_value_list[i]

    # return the dict
    return new_dict


# signature line for favorite_color() function
def favorite_color(input_dict: dict[str, str]) -> str:
    """Function that returns the crowd's favorite color."""
    # initial setup
    val_list: list[str] = list()
    repetition_counter: int = 0
    repetition_list: list[int] = list()
    current_max: int = 0
    max_index: int = 0
    repetition_list_1: list[int] = list()

    # make sure list isn't empty
    if len(input_dict) == 0:
        return "None"

    # loop through to get a list of vals
    for key in input_dict:
        val_list.append(input_dict[key])
    
    # check if we have repeats
    for i in range(0, len(val_list), 1): 
        for j in range(0, len(val_list), 1):
            if val_list[i] == val_list[j]:
                repetition_counter += 1

        # make list of counts
        repetition_list_1.append(repetition_counter)
        repetition_counter = 0

    # initalize max_val
    max_val: int = repetition_list_1[0]

    # loop through rep_list_1 
    for val in repetition_list_1:
        if max_val < val:
            max_val = val

    if max_val < 2:
        for elem in input_dict:
            return input_dict[elem]
        
    # update repetition counter to 0
    repetition_counter = 0

    # check counts of colors in dictionary
    for i in range(0, len(val_list), 1):
        for j in range(0, len(val_list)):
            if val_list[i] == val_list[j]:
                repetition_counter += 1
        
        repetition_list.append(repetition_counter)
        repetition_counter = 0
    
    # need first index
    i: int = 0

    # the index of the max value in repeition_list is the index in val list we need to return
    current_max = repetition_list[i]
    for i in range(0, len(repetition_list), 1):
        if current_max < repetition_list[i]:
            current_max = repetition_list[i]
            max_index = i
    
    return val_list[max_index]


# signature line for count() function
def count(input_list: list[str]) -> dict[str, int]:
    """Function that determines how many time something is in a list."""
    output_dict: dict[str, int] = dict()
    repetition_counter: int = 0
    empty_dict: dict[str, int] = dict()

    # return empty dict if len of input dict is 0
    if len(input_list) == 0:
        return empty_dict
    
    # store keys and intialize values
    for i in range(0, len(input_list), 1):
        if not (input_list[i] in output_dict): 
            output_dict[input_list[i]] = 0

    # store values
    for i in range(0, len(input_list), 1):
        for j in range(0, len(input_list), 1):
            if input_list[i] == input_list[j]:
                repetition_counter += 1
        output_dict[input_list[i]] = repetition_counter
        repetition_counter = 0

    return output_dict


# signature line for alphabetizer
def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Function that takes a list and returns letter and list of words starting with letter."""
    output_dict: dict[str, list[str]] = dict()
    empty_dict: dict[str, list[str]] = dict()

    # return empty dict if len of input dict is 0
    if len(input_list) == 0:
        return empty_dict

    # store keys and intialize values
    for i in range(0, len(input_list), 1):
        if not (input_list[i] in output_dict): 
            current_str = input_list[i]
            current_str.lower()
            output_dict[current_str[0]] = list()

    # store words that start with letter
    for elem in output_dict:
        for i in range(0, len(input_list), 1):
            current_str = input_list[i]
            if elem == current_str[0].lower():
                output_dict[elem].append(input_list[i])
    
    # retrun dict
    return output_dict


# signature line for update_attendence() function
def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Function that changes a dict based on inputs."""
    # initial setup
    check: int = 0
    student_list: list[str] = list()
    student_list.append(student)

    # check if day is already in there
    for elem in input_dict:
        if elem == day:
            check = 1

    # if check is 0 store the day and the studen
    if check == 0:
        input_dict[day] = student_list

    # if check is 1, day is already in there
    if check == 1:
        input_dict[day].append(student)

    # return the dictionary
    return input_dict