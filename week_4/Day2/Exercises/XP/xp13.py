all_ages = []

user = input("Input your age. When your done type 'exit':  \n")
while user != 'exit':
    if int(user) >= 16:
        all_ages.append(user)
    user = input("Input your age. When your done type 'exit':  \n")
print(all_ages)
