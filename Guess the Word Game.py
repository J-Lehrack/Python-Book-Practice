# Game where the player will guess a randomly chosen word
# by being allowed to guess 5 letters then guessing the word

import random

WORDS = ("eagles", "forward", "skyrim", "coushatta", "jupiter", "tesla")
word = random.choice(WORDS)
guess = word
attempts = 0

for letter in word:
    letter_guess = input("Guess a letter in the word: ")
    if letter_guess in word:
        print("That letter is in the word\n")
    else:
        print("That letter is not in the word\n")

    attempts += 1

    while attempts >= 5:
        input("\nNow guess the word: ")
        if guess == word:
            print("Congratulations! You guessed the word!")
            break
        else:
            print("Sorry, better luck nice time")
            break
        print("Well played")