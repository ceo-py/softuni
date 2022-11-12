from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.astronaut_name(value)
        self.__name = value

    @abstractmethod
    def breathe(self):
        ...

    def increase_oxygen(self, amount: int):
        ...

