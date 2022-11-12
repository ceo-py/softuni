from project.validation.validation import Validation


class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.race_name(value)
        self.__name = value
