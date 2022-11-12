from project.validation.validation import Validation


class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.driver_name(value)
        self.__name = value
