user_input = input("Type one number in here...")
result = 0
for i in range(1,5):
    result += int(user_input*i)
    print(user_input*i)
print(result)
