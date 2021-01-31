# Exercise 5
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

active = True

while active:
    topping = input("Please enter a topping that you would like (enter 'quit' when you are finished): ")
    if topping == 'quit':
        active = False
    elif topping == 'leave me alone':
        active = False
    elif topping == 'stop':
        active = False
    else:
        print(f"You chose {topping}")

print("Goodbye !")
