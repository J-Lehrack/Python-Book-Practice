# Calculating tips at a restaurant

drinks = float(input("How much did the drinks cost?\n"))

entree = float(input("How about the entree?\n"))

dessert = float(input("And lastly, the dessert?\n"))

tips = drinks + entree + dessert

print("\nList of potential tips:")
print("For 5%:", round(tips*.05,2), "\n",
    "For 10%:", round(tips*.1,2), "\n",
    "For 15%:", round(tips*.15,2), "\n",
    "For 20%:", round(tips*.2,2), "\n",)