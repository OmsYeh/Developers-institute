# Exercise 4

import random


def random_number(x):
    second = random.randint(1, 100)
    if x == second:
        print("Well done you guessed the same number!")
    else:
        print("Better luck next time, the numbers are not the same")
        print(f"your number is {x}")
        print(f"the generated number is {second}")
