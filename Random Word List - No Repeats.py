# A list of words printed in random order without repeating.

import random

WORDS = ["Button", "Heaven", "Work", "Taste", "Party", "Worm"]


while len(WORDS) != 0:
    word = random.choice(WORDS)
    print(word)
    WORDS.remove(word)