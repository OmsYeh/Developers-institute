# Exercise 4
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase
# "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

m_names = ["Harry", "Hermione", "Ronald", "Neville"]


def show_magicians(*args):
    for name in args:
        make_great(*m_names)


def make_great(*args):
    for name in args:
        print(f'{name} The Great')


show_magicians(m_names)
