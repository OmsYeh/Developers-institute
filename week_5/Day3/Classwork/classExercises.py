# Exercise
# Analyse this code. What will be the output ?
#
# Explain the goal of the methods
#
# Create a method that modifies the name of the person


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_greet(self):
        print("Hello my name is " + self.name)

    def rename(self,new_name):
        self.name = new_name
        print(self.name)


p1 = Person("John", 36)
p1.self_greet()
p1.rename("Omri")

# output will be:
# Hello my name is John
