matrix =[
    [7, " ", 3],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', " ", '#'],
    ['s', 'M', " "],
    ['$', 'a', " "],
    ['#', 't', '%'],
    ['i', 'r', '!']
]

text = ' '
invalid_char_count = 0


def is_valid(char):
    return type(char) is str and char.isalnum()


for column in range(3):
    for row in matrix:
        char = row[column]

        if is_valid(char):
            if invalid_char_count > 1:
                invalid_char_count = 0
                text += ' '
            text += char
        else:
            invalid_char_count += 1


print(text)

# If we find an invalid character, we just count it.
# If we find a valid character:
# then if we have more than 1 invalid characters in a row,
# we add a space to the text, and reset the invalid character count.
# Then we add it to the text.

