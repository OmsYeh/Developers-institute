menu = input("Type input here -->: ")
existing = []
while menu != "Exit":
	if menu == "Add a name":
		new_name = input("Please type name here: ")
		existing.append(new_name)
		menu = input("Type input here -->: ")
	if menu == "Remove an existing name":
		existing_name = input("Please type name here: ")
		existing.remove(existing_name)
		menu = input("Type input here -->: ")
	if menu == "":
		menu = input("Type input here -->: ")
	if menu == "View family members":
		counter = 0
		print("These are your family names: ")
		for name in existing:
			name.capitalize()
			counter += 1
			print(name.capitalize(), end="")
			if name != existing[-1]:
				print(",")
			if name == existing[-2]:
				print("and")
			if name == existing[-1]:
				print(".")
		menu = input("Type input here -->: ")

