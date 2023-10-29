"""Returns list of words that are shorter than 5 characters."""


def short_words(input_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    output_list: list[str] = list()

    for i in range(0, len(input_list), 1):
        if len(input_list[i]) < 5:
            output_list.append(input_list[i])
        else:
            print(f"{input_list[i]} is too long!")

    return output_list


my_list: list [str] = ["sun", "cloud", "sky"]

print(short_words(my_list))