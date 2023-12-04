from csv import DictReader

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


print(read_csv_rows("test_data.csv"))

