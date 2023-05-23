# Guess the number PVP version! User against the Computer

import random

answer = random.randint(1,100)
user_guess = int(input("Guess your number: "))
comp_guess = random.randint(1,100)
a = None
print("Computer Guess: ", comp_guess)

while user_guess != answer or comp_guess != answer:
    if user_guess > answer:
        print("Lower")
    elif user_guess < answer:
        print("Higher")
    elif user_guess == answer:
        print("Congratulations Player 1!!")

    elif comp_guess > answer:
        print("Lower")
        a = comp_guess
        comp_guess = random.randint(1,a)
    elif comp_guess < answer:
        print("Higher")
        comp_guess = random.randint(comp_guess,a)
    elif comp_guess == answer:
        print("Ouch, maybe next time Player 1")

    user_guess = int(input("Guess your number: "))
    print("Computer guess:", comp_guess)

print("A well played match, wouldn't you say?")

input("\n\nPress Enter to end game.")
