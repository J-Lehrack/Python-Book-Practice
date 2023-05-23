# Enter a person's name and return their fathers name

father_son = {"Luke Skywalker": "Darth Vader", "Gimli": "Gloin", "Tony Stark": "Howard Stark"}

choice = None
while choice != "0":

    print(
    """
    Who's Your Daddy
    
    0 - Quit
    1 - Look Up a Father-Son pair
    2 - Add a pair
    3 - Adjust a pair
    4 - Delete a pair
    """
    )

    choice = input("Choice: ")

    if choice == "0":
        print("Hope you learned something")
        print("Goodbye!")

    elif choice == "1":
        son = input("Who's father would you like to know?: ")
        if son in father_son:
            father = father_son[son]
            print("The father of", son, "is", father)
        else:
            print("That father-son duo is not known. Try adding it!")

    elif choice == "2":
        son = input("What is the name of the son you want to add?: ")
        if son not in father_son:
            father = input("What is his father's name: ")
            father_son[son] = father
            print("\n", son, "has been added.")
        else:
            print("\n That duo already exists! Try re-naming it.")

    elif choice == "3":
        son = input("Who's father needs to be changed?: ")
        if son in father_son:
            father = input("What is his father's name?: ")
            father_son[son] = father
            print("\n", father, "has been renamed.")
        else:
            print("\n That son isn't in the list! Try adding it")

    elif choice == "4":
        son = input("Which duo do you want to remove from the list?: ")
        if son in father_son:
            del father_son[son]
            print("\n", son, "and his father have been removed")
        else:
            print("\nI can't do that!", son, "isn't in the list.")

    else:
        print("\n Sorry, but", choice, "isn't a valid choice.")