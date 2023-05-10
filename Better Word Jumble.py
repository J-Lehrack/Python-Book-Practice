# Word Jumble with hints and a scoring system
# based on if you used the hints or not

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = random.choice(WORDS)
correct = word
attempts = 0

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
    """
               Welcome to Word Jumble!
    
       Unscramble the letters to make a word.
        Try for as few attempts as possible.
            (Beware! Hints add points!)
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.\n")

    hint_prompt = input("Would you like a hint? ")
    if hint_prompt == "Yes":
        print("The word starts with:", correct[0])
        attempts += 3
    elif hint_prompt == "No":
        print("I believe in you!")

    guess = input("Your guess: ")
    attempts += 1
    score = attempts

if guess == correct:
    print("That's it!  You guessed it!\n")
    print("Your score is:", score)

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
