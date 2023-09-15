"""ex02_one_shot_wordle"""
__author__ = "730695813"
# initialization of variables
secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
counter_1: int = 0
result_string: str = "" # setting initial resultant string to blank
# error and retry method if length of characters is wrong
while (len(user_guess) != len(secret_word)):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
# return string if guess is wrong
if secret_word != user_guess:
   print("Not quite. Play again soon!")
# if secret word and user input matches, then this message is printed out
elif secret_word == user_guess:
   print("Woo! You got it!")
# iterating over each character within each respective strings
while (counter_1 < 6):
   # check if characters are in both strings and in correct places
   if (secret_word[counter_1] == user_guess[counter_1]):
     result_string += GREEN_BOX
   # check if characters may be in both strings but in the wrong places
   elif (secret_word[counter_1] != user_guess[counter_1]):
      # counter for secret word
      counter_2: int = 0
      # iterating over secret word and checking one character within the user input
      while(counter_2 < 6):
         # if counter_2 index of secret word is equal to index counter of user_input_1 print yellow box then set counter_2 so while loop ends
         if (user_guess[counter_1] == secret_word[counter_2]):
            result_string += YELLOW_BOX 
            counter_2 = 5
         # if counter_2 index of secret word is not equal to index counter of user_input_1, do nothing until it's the last iteration/check of secret word. Then print white box
         elif (user_guess[counter_1] != secret_word[counter_2]):
            if (counter_2 == 5):
               result_string += WHITE_BOX
         # increment counter_2
         counter_2 += 1
   # increment counter
   counter_1 += 1
# print the resultant string
print(result_string)