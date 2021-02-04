active = True
toppings = []
while active:
	user_input = input("Please enter a topping that you would like (enter 'quit' when you are finished): ")
	if user_input == 'quit' or user_input == 'leave me alone' or user_input == "stop":
	    active = False
	else:
		toppings.append(user_input)
		print(f"I'll add {user_input} to your pizza")

total_price = (len(toppings) * 2.5) + 10

print(f"Your total price for the pizza is: {total_price}")