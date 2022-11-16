from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def make_sound(self):
        ...


class Cat(Animal):

    def make_sound(self):
        return "Meow"


class Dog(Animal):

    def make_sound(self):
        return "Woof-woof"


animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())