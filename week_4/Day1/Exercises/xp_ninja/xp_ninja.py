# Exercise 1

# After calling Python3 we can state where the file that we want opened is by describing the Path so using this we can call Python3 anywhere




# Exercise 2

# alias py=python3




# Exercise 3

    # >>> 3 <= 3 < 9 --------------------------- True
    # >>> 3 == 3 == 3 -------------------------- True
    # >>> bool(0) ------------------------------ Fasle
    # >>> bool(5 == "5") ----------------------- Fasle
    # >>> bool(4 == 4) == bool("4" == "4") ----- True
    # >>> bool(bool(None)) --------------------- Fasle
    # x = (1 == True) -------------------------- True
    # y = (1 == False) ------------------------- Fasle
    # a = True + 4 ----------------------------- 5 
    # b = False + 10 --------------------------- 10

    # 	None of these will run becasue the unquoted letters are undefined
    # print("x is", x) ------------------------- x is undefined
    # print("y is", y) ------------------------- y is undefined
    # print("a:", a) --------------------------- a is undefined
    # print("b:", b) --------------------------- b is undefined




# Exercise 4

# my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum."""

# len(my_text)




# Exercise 5

# longest = 0
# user_text = input("Type a sentence without the character 'A' in it: ")
# if "A" not in user_text:
# 	if len(user_text) > longest:
# 		longest = user_text
# 		print("Congrats on breaking the record!")
# else:
# 	print("There is an 'A' in there somewhere...")

