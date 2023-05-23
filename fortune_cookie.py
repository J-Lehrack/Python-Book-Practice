# Script that provides a randomly generated fortune

import random

input("Press Enter and receive a fortune:\n")

fortune = random.randint(1,5)

while 0 < fortune < 6:
    if fortune == 1:
        print("You will find great success in your career.")

    elif fortune == 2:
        print("Make friends of your enemies.")

    elif fortune == 3:
        print("Do or do not, there is no try.")

    elif fortune == 4:
        print("Where there is a will, there is a way.")

    elif fortune == 5:
        print("GO ASK THAT PERSON OUT ALREADY!")

    input("\nPress Enter and receive your next fortune:\n")
    fortune = random.randint(1,5)