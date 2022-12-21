from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Meal(ABC):
    correct_meals = ("Starter",
                     "MainDish",
                     "Dessert")

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.len_of_item_less(value, 1, "value error", "Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.number_less_then_or_equal(value, 0.0, "value error", "Invalid price!")
        self.__price = value

    def reduce_quantity(self, quantity: int):
        self.quantity -= quantity

    def add_quantity(self, quantity: int):
        self.quantity += quantity

    @abstractmethod
    def details(self):
        pass
