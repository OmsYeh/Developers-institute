# Exercise 1:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def oldest_cat(*cats):
        oldest = 0
        cats = list(cats)
        for cat in cats:
            if cat.age > oldest:
                oldest = cat.age
        return f'The Oldest cat is {oldest} years old'


my_cat = Cat("Corey", 1)
gila_cat = Cat("Charlie", 7)
tzios_cat = Cat("Niki", 8)

Cat.oldest_cat(my_cat, gila_cat, tzios_cat)


# Exercise 2

class Dog:
    def __init__(self, name_dog, height_dog):
        self.name = name_dog
        self.height = height_dog

    def talk(self):
        return 'Woof'

    def jump(self):
        return f'{self.name} can jump {self.height *2} meters high'


davids_dog = Dog("Rex", 0.50)
davids_dog.jump()
davids_dog.talk()
sarahs_dog = Dog('Teacup', 0.20)
sarahs_dog.jump()
sarahs_dog.talk()


def tallest_dog(*dogs):
    tallest = 0
    dogs = list(dogs)
    for dog in dogs:
        if dog.height > tallest:
            tallest = dog.height
            return f'The tallest dog is {tallest} meters tall'


tallest_dog(davids_dog, sarahs_dog)

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


class Song:
    def __init__(self, lyrics):
        pass

    def sing_me_a_song(self, lyrics):
        happy_bday = Song(["Have a sunshine on you,", "Happy Birthday to you !"])
