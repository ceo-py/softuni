from abc import ABC, abstractmethod

from project.validation.validation import Validation


class BaseFish(ABC):

    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_string(value, "Fish name")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validation.empty_string(value, "Fish species")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.number_below_zero(value)
        self.__price = value

    @abstractmethod
    def eat(self):
        ...

