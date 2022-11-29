from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.name_horse_less_than_4(value, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validation.speed_limit(value, self.maximum_speed, "Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        ...



