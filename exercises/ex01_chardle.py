"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730695813"
counter: int = 0
user_string: str = input("Enter a 5-character word: ")
user_character: str = input("Enter a single character: ")
if (len(user_string) != 5):
    print("Error: Word must contain 5 characters")
    exit()
if (len(user_character) != 1):
    print("Error: Character must be a single character")
    exit()
print("Searching for " + str(user_character) + " in " + str(user_string))
if (user_string[0] == user_character):
    print(user_character + " found at index 0")
    counter += 1
if (user_string[1] == user_character):
    print(user_character + " found at index 1")
    counter += 1
if (user_string[2] == user_character):
    print(user_character + " found at index 2")
    counter += 1
if (user_string[3] == user_character):
    print(user_character + " found at index 3")
    counter += 1
if (user_string[4] == user_character):
    print(user_character + " found at index 4")
    counter += 1
if counter == 0:
    print("No instances of " + user_character + " found in " + user_string)
if counter == 1:
    print("1 instance of " + user_character + " found in " + user_string)
else:
    print(str(counter) + " instances of " + user_character + " found in " + user_string)