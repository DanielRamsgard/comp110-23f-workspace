

def odd_and_even(input_list: list[int]) -> list[int]:
    """Function takes input returns list with odds at even indexes."""
    new_list: list[int] = list()
    
    for i in range(0, len(input_list), 1):
        if (input_list[i] % 2 == 1) and (i % 2 == 0):
            new_list.append(input_list[i])

    return new_list


test = [7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]

print(odd_and_even(test))