# A fantasy character creation program, distributing points to 4 separate resources

attributes = {"Strength": 0,
                "HP": 0,
                "Wisdom": 0,
                "Dexterity": 0}

choice = None
total_stats = int(attributes["Strength"] + attributes["HP"] + attributes["Wisdom"] + attributes["Dexterity"])
while choice != "0" and total_stats <= 30:

    print(
        """
        Allocate your points:
    
        0 - Ready to Start
        1 - Add points to a Stat
        2 - Remove points from a Stat
        """
    )
    total_stats = int(attributes["Strength"] + attributes["HP"] + attributes["Wisdom"] + attributes["Dexterity"])
    choice = input("Choice: ")

    if choice == "0":
        if total_stats < 30:
            print("You haven't used all your points")
            print(30-total_stats, "remaining")
            print("Best of luck to you adventurer!")
        else:
            print("Your stats are:", attributes)
            print("Your adventure begins!")


    elif choice == "1":
        stat_add = input("What Stat do you want to add points to?: ")
        add_number = int(input("How many points do you want to add: "))
        if stat_add in attributes and 0 < add_number + total_stats <= 30 and add_number > 0:
            attributes[stat_add] += add_number
            print("\n", add_number, "points have been added to", stat_add)
            print(stat_add, "has", attributes[stat_add], "points total")
            print("\nCurrent stat total is:", total_stats + add_number)
        elif total_stats + add_number > 30:
            print("You only have 30 points to use!")
        elif add_number + total_stats < 0:
            print("You can't have negative points!")
        elif add_number < 0:
            print("No negative points allowed!")
        else:
            print("\nThat Stat doesn't exist!")

    elif choice == "2":
        stat_remove = input("What Stat do you want to remove points from?: ")
        subtract_number = int(input("How many points do you want to remove: "))
        if stat_remove in attributes and 0 < total_stats - subtract_number <= 30 and subtract_number > 0:
            attributes[stat_remove] -= subtract_number
            print("\n", subtract_number, "points have been added to", stat_remove)
            print(stat_remove, "has", attributes[stat_remove], "points total")
            print("\nCurrent stat total is:", total_stats - subtract_number)
        elif total_stats - subtract_number < 0:
            print("You can't have negative points!")
        elif total_stats - subtract_number > 30:
            print("You only have 30 points to use")
        elif subtract_number < 0:
            print("No negative points allowed!")
        else:
            print("\nThat Stat doesn't exist!")

    else:
        print(choice, "doesn't exist")
