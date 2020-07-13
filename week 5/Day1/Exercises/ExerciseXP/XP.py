# Exercise 1:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


main_cats = [
    Cat("Corey", 3),
    Cat("Charlie", 4),
    Cat("Clyde", 1)
]


def oldest_cat():
    cat_age = 0
    for cat in main_cats:
        if cat.age > cat_age:
            cat_age = cat.age

    print(f'The oldest cat is {cat_age} years old.')


oldest_cat()


# Exercise 2
# Create a class Dog
# In this class, create a method __init__, that takes two parameters : nameDog
and heightDog. This function initialises two attributes with the values of the parameters.
# Create a method talk that prints Woof
# Create a method jump that multiplies by two the height of the dog. Print the height of the dog when he jumps.
# Create an object Davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object Sarahs_dog. His dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Check which dog is bigger. Than add to this dog a characteristic ‘winner’ that is a Boolean.

class Dog():
    species = 'mammal'

    def __init__(self, name, height):
        self.name = name
        self.height = height