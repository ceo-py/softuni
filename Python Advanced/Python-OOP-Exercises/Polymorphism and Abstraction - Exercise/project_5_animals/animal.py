from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.age = age
        self.name = name
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass