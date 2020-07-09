# Exercise 3
# Write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


shirt_size = "Medium"
shirt_print = "This Shirt is soooo dope!"


def make_shirt(size="Large", text="I love Python"):
    print(f'Hey! your shirt will be size {size} and it will print {text}')


print(make_shirt("Medium", 'This shirt is dope!'))
print(make_shirt(shirt_size, shirt_print))


print(make_shirt("Large", text="I love Python"))
print(make_shirt("Medium", text="I love Python"))
print(make_shirt("Small §§§", text="I love Coding"))
