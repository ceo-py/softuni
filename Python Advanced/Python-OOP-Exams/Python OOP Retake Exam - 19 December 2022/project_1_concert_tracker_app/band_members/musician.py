from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Musician(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_string_or_white_space(value, "Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.check_number_less_than(value, 16, "Musicians should be at least 16 years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        pass