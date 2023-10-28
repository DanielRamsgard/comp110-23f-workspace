"""guess_game."""
from random import randint
secret: int = randint(1, 10)
guess: int = int(input("guess a number between 1 and 10: "))
if (guess < 1 or guess > 10):
    print("not between one and 10)")
    exit()
while guess != secret:
    print("Wrong!")
    if guess < secret:
        print("too low")
    elif guess < secret:
        print("too high")
    guess = int(input("Guess again: "))
print("You guess correctly!")