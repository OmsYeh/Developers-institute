# Exercise 6

name = "Omri"
user = input("Guess my name here:  ")
your_name = user.capitalize()
while your_name != name:
    print("Not the same name")
    user = input("Guess my name here:  ")
    your_name = user.capitalize()
else:
    print("well done you guessed my name")

