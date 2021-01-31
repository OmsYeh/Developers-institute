# Exercise 6

cost=0

number_of_family_members = int(input("How mway members in your family want to buy a ticket for the movie?"))

for i in range(number_of_family_members):
    age = int(input("what is your age?"))
    if age <= 3:
        print("your ticket is free!")
        continue
    elif age > 3 and age <= 12:
        cost += 10
    else:
        cost += 15
print(f"your total price for the tickets is {cost}")



teens = int(input("How many are you?"))
teens_of_age = []
for i in range(teens):
    teen_age = int(input("what is your age?"))
    if teen_age < 16:
        print("you are too young for this movie!")
        teens_of_age.append(teen_age)
    elif teen_age > 16 and teen_age < 21:
        print("Enjoy the movie!")
        teens_of_age.append(teen_age)
    else:
        print("you're too old for this shit...")
        teens_of_age.append(teen_age)
        print(teens_of_age)
