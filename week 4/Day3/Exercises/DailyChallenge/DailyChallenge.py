users_string = input("please enter a sentence:")
action = input('please choose encrypt("e") or decrypt("d"):')
letter_list = []
outcome = ""
if action == "e":
    for letter in users_string:
        if letter != " ":
            letter_list += [ord(letter) + 3]
        else:
            letter_list += [ord(letter)]
    for num in letter_list:
        outcome += chr(num)
    print(outcome)
else:
    for letter in users_string:
        if letter != " ":
            letter_list += [ord(letter) - 3]
        else:
            letter_list += [ord(letter)]
    for num in letter_list:
        outcome += chr(num)
    print(outcome)
