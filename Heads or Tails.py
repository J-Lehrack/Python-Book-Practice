# A program that simulated a coin flip

import random

heads = 0
tails = 0
total_flips = 0

while total_flips < 100:
    toss = random.randint(1,2)
    if toss == 1:
        print("Heads")
        heads += 1
        total_flips += 1

    elif toss == 2:
        print("Tails")
        tails += 1
        total_flips += 1

print("The number of heads is: ", heads)
print("The number of tails is: ", tails)