# Exercise 12

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


all_ages = []

user = input("Input your age. When your done type 'exit':  \n")
while user != 'exit':
    if int(user) < 16:
        all_ages.append(user)
        print("You are too young for this movie!")
    elif int(user) >= 16 and int(user) <= 21:
        all_ages.append(user)
        print("Enjoy the movie!")
    else:
        all_ages.append(user)
        print("You're too old for this shit...")
    user = input("Input your age. When your done type 'exit':  \n")
print(all_ages)
