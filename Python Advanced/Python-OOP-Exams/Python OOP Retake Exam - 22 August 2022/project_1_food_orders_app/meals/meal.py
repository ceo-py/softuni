from abc import ABC, abstractmethod

from project.func.validations import Validation


class Meal(ABC):

    @abstractmethod
    def __init__(self, name: str, price: float, quantity):
        self.quantity = quantity
        self.price = price
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validation.empty_string(value):
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if Validation.check_positive_number(value):
            self.__price = value

    def details(self):
        name = self.__class__.__name__
        if name == "MainDish":
            name = "Main Dish"

        return f"{name} {self.name}: {self.price:.2f}lv/piece"
