"""Card counting"""
user_input = input("Guess number: ")
int_user_input = int(user_input)
if (int_user_input == 10):
    print("Nice job; you guessed it right. Here's a cookie ::")
else: 
    print("rerun and guess again")