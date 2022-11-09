from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Horse(ABC):
    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.name_horse(value)
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validation.speed_horse(value, self.maximum_speed)
        self.__speed = value

    def train(self):
        if self.speed + self.train_gain > self.maximum_speed:
            self.speed = self.maximum_speed
        else:
            self.speed += self.train_gain
