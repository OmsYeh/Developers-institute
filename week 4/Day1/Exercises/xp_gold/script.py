# 1
"""
it is possible to access python3 even outside of an executable directory because
python3 will search for all executable files within the path that it is situated on.
"""
# 2
# you can open a python console by typing in the terminal python3 then the name of the python file.
# 3
# print(("hello world\n" * 4), ("i love python\n" * 4))


user_input = input("Type one number in here...")
result = 0
for i in range(1,5):
    result += int(user_input*i)
    print(user_input*i)
print(result)
