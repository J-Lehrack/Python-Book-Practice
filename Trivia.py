# Attempting to program random trivia facts about a person

print("What is your name?")

user = input()

print(user, ", how tall are you in feet? (Use decimals)")

height = float(input())

print("Last question", user, ", about how many hours are you on your phone each day?")

phone_use = float(input())

print("At", height, "feet you are", \
        round(height*12,2), "inches tall,"\
        "and", round(height*30.48,2), "cm tall.")

print("And, by using your phone for", \
      phone_use, "hours each day,", \
      "you are using your phone for:\n",
        phone_use*7, "hours each week\n",
        phone_use*7*4, "hours each month\n",
        "and,", phone_use*365, "every year!!")