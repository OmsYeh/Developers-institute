# Exercise 1:

#
# class Cat:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def oldest_cat(*cats):
#         oldest = 0
#         cats = list(cats)
#         for cat in cats:
#             if cat.age > oldest:
#                 oldest = cat.age
#         return f'The Oldest cat is {oldest} years old'
#
#
# my_cat = Cat("Corey", 1)
# gila_cat = Cat("Charlie", 7)
# tzios_cat = Cat("Niki", 8)
#
# Cat.oldest_cat(my_cat, gila_cat, tzios_cat)
#
#
# # Exercise 2
#
# class Dog:
#     def __init__(self, name_dog, height_dog):
#         self.name = name_dog
#         self.height = height_dog
#
#     def talk(self):
#         return 'Woof'
#
#     def jump(self):
#         return f'{self.name} can jump {self.height *2} meters high'
#
#
# davids_dog = Dog("Rex", 0.50)
# davids_dog.jump()
# davids_dog.talk()
# sarahs_dog = Dog('Teacup', 0.20)
# sarahs_dog.jump()
# sarahs_dog.talk()
#
#
# def tallest_dog(*dogs):
#     tallest = 0
#     dogs = list(dogs)
#     for dog in dogs:
#         if dog.height > tallest:
#             tallest = dog.height
#             return f'The tallest dog is {tallest} meters tall'
#
#
# tallest_dog(davids_dog, sarahs_dog)

# Exercise 3
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments:
#
# self
# lyrics : a list.
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Define a varible:
# happy_bday = Song(["Have a sunshine on you,",
#                    "Happy Birthday to you !"])

# Call the sing_me_song method on this variable.

#
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for strip in self.lyrics:
#             print(strip)
#
#
# happy_bday = Song(["Have a sunshine on you,", "Happy Birthday to you !"])
# happy_bday.sing_me_a_song()


# Exercise 4

# Create a method sort_animal that sorts the animals. Each animal, depending on its first letter should be
# placed inside a pen. { 1: "Ape", 2: ["Baboon", Bear"]}

# Create a method get_pen that prints the list of animals inside each pen.
# Create an object ramatGanSafari and call all the methods.

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print('Animal already exists')
        else:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        for animal in self.animals:
            if animal == animal_sold:
                print(f'Goodbye our dear friend, {animal_sold}')
                self.animals.remove(animal)
                print("Animal Removed from list")

    def sort_animal(self):
        self.animals.sort()
        for letter in "ABC"


my_zoo = Zoo('Omris Zoo')

my_zoo.add_animal("cheetah")
my_zoo.add_animal("zebra")
my_zoo.add_animal("monkey")
my_zoo.add_animal("fish")
my_zoo.add_animal("Lion")
my_zoo.get_animals()

my_zoo.sell_animal('Lion')
my_zoo.get_animals()
