# Critter Caretaker
# A virtual pet to care for

import random


class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        happiness_level = self.hunger + self.boredom
        if happiness_level < 5:
            hp = "happy"
        elif 5 <= happiness_level <= 10:
            hp = "okay"
        elif 11 <= happiness_level <= 15:
            hp = "frustrated"
        else:
            hp = "mad"
        return hp

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, hour):
        print("Wheee!")
        self.boredom -= hour
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        return self.name, self.mood, self.hunger, self.boredom


def main():
    crit_name1 = input("What do you want to name critter 1?: ")
    crit_name2 = input("What do you want to name critter 2?: ")
    crit_name3 = input("What do you want to name critter 3?: ")
    crit = Critter([crit_name1, crit_name2, crit_name3])

    choice = None
    while choice != "0":
        print(
            """
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            food = int(input("How many bowls of food do you want to give?: "))
            crit.eat(food)

        # play with your critter
        elif choice == "3":
            hour = int(input("How many hours do you want to play?: "))
            crit.play(hour)

        # hidden choice to check attributes
        elif choice == "4":
            print(crit.name, "has the following attributes:")
            print(crit.__str__())

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
input("\n\nPress the enter key to exit.")
