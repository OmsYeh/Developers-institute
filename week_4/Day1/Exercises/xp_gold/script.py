# Exercise 1

# print("hello world\n" * 4 + "i love python\n" * 4)


# Exercise 2

seasons = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]

user_input = int(input("Please provide a month represented by it's number"))

if user_input in seasons[0]:
	print("The Season at this month will be: Spring")
elif user_input in seasons[1]:
	print("The Season at this month will be: Summer")
elif user_input in seasons[2]:
	print("The Season at this month will be: Autumn")
elif user_input in seasons[3]:
	print("The Season at this month will be: Winter")

print("Enjoy the weather")