class Animal:
    lives = 1

    def eat():
        print("OM NOM NOM")

class Cat(Animal):
    lives = 9
    species = "Felis catus"
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("meow " + self.name)    

class Dog(Animal):
    species = "Canis"

    def greet(self):
        print("woof")

class Test(object):
    i = 3

    
