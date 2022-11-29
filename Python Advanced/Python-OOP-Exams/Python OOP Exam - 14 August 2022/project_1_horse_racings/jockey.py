from project.validation.validation import Validation


class Jockey:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.name_empty_string_or_white_spaces(value, "Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.jokey_age_over_17(value, "Jockeys must be at least 18 to participate in the race!")
        self.__age = value

