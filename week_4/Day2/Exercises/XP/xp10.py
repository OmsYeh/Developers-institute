user_input = input("What are your favourite fruit, please seperate each one with a space: ")
fav_fruit = user_input.split(" ")


user_in_fruitbowl = input("Type a fruit to see if it's in your fruit bowl: ")
if user_in_fruitbowl in fav_fruit:
	print("You chose one of your favorite fruits! Enjoy!")
else:
	print("You chose a new fruit. I hope you enjoy it too!")


counter = 0
print("These are your fruit: ")
for fruit in fav_fruit:
	fruit.capitalize()
	counter += 1
	print(fruit.capitalize(), end="")
	if fruit != fav_fruit[-1]:
		print(",")
	if fruit == fav_fruit[-2]:
		print("and")
	if fruit == fav_fruit[-1]:
		print(".")
