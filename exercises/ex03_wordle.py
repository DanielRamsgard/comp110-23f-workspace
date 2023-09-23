"""This code is for the ex03_wordle exercise."""
__autho__ = "730695813"
# initializing emoji variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# signature line for contains_char function
def contains_char(input_str: str, input_chr: str)->bool: 
    """Function returns True if input_chr is found at any index of input_str: False otherwise."""
    assert len(input_chr) == 1
    # initializing idex variable
    i: int = 0
    # iterating over secret string to check if the input_chr is anywhere inside of input_str
    while(i < len(input_str)):
        if (input_str[i] == input_chr):
            return True
        i += 1
    return False
# signature line for emojified function
def emojified(input_guess: str, secret_str: str)->str: 
    """Function to return string of emojis specifying yellow, green, and white boxes."""
    assert len(input_guess) == len(secret_str)
    # initializing idex variable and return value
    i: int = 0
    result_str: str = ""
    # loop to iterate over input_guess and secret_str variables: assigns relative emoji boxes based on checks
    while(i < len(input_guess)):
        if (input_guess[i] == secret_str[i]):
            result_str += GREEN_BOX
        elif (contains_char(secret_str, input_guess[i]) == True):
            result_str += YELLOW_BOX
        elif (contains_char(secret_str, input_guess[i]) != True):
            result_str += WHITE_BOX
        i += 1
    return result_str
# signature line for function to make sure guess lengths are correct relative to secret word
def input_guess(input_int: int)->str:
    """Function to determine if user guess matches the desired len of the secret word."""
    # initializing input string
    input_str: str = input(f"Enter a {input_int} word: ")
    # loop to keep asking for an input string that matches length of secret word
    while (len(input_str) != input_int):
        new_input_str: str = input(f"That wasn't {input_int} chars! Try again: ")
        if (len(new_input_str) == input_int):
            return new_input_str
    return input_str
# signature line for main function
def main()->None:
    """The entry point of the game and the main game loop."""
    # initializing variables
    secret_word: str = "codes"
    correct_guess: str = "\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9"
    turn: int = 1
    # loop to fun game and increment # of turns
    while(turn < 7):
        # function to check input string length
        input_str = input_guess(len(secret_word))
        # prints turn and result_str
        print(f"=== Turn {turn}/6 ===")
        print(emojified(input_str, secret_word))
        # if correct guess, prints the following and exits game
        if (emojified(input_str, secret_word) == correct_guess):
            print(f"You won in {turn}/6 turns!")
            exit()
        # if turns is equal to 6, program exits 
        elif (turn == 6):
            print("X/6 - Sorry, try again tomorrow!")
            exit()
        turn += 1
if __name__ == "__main__":
    main()