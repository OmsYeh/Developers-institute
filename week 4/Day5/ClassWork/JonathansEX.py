text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris  isi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit  sse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt  n culpa qui officia deserunt mollit anim id est laborum."""


def num_of_words(lor):
    lenght = len(text.split())
    return lenght


num_of_words(text)

def num_of_char(string, character):
    char_count = 0
    for char in string:
        if char == character:
            char_count += 1
            return(char_count)


num_of_char(text,"a")