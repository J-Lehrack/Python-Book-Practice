# Game where the player will guess a randomly chosen word
# by being allowed to guess 5 letters then guessing the word

import random

WORDS = ("eagles", "forward", "skyrim", "coushatta", "jupiter", "tesla")
word = random.choice(WORDS)
attempts = 0

while attempts != 6:

    attempts += 1

    if attempts < 6:
        letter_guess = input("Guess a letter in the word: ")
        if letter_guess in word:
            print("That letter is in the word\n")
        else:
            print("That letter is not in the word\n")

    elif attempts == 6:
        guess = input("Guess the word: ")
        if guess == word:
            print("Congratulations! You guessed the word!")
        else:
            print("Sorry, better luck nice time")

    else:
        print("Thank you for playing")