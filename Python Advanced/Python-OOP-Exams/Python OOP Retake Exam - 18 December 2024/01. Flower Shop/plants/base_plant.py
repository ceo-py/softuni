from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BasePlant(ABC):
    def __init__(self, name: str, price: float, water_needed: int):
        self.name = name
        self.price = price
        self.water_needed = water_needed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.empty_string_or_empty_spaces(
            value, "Plant name cannot be null or empty!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        Validation.is_number_equal_or_under(
            value, 0.0, "Price must be greater than zero!")
        self.__price = value

    @property
    def water_needed(self):
        return self.__water_needed

    @water_needed.setter
    def water_needed(self, value: int):
        Validation.is_number_in_range_of_two_numbers(
            value, 1, 2000, "Water needed must be between 1 and 2000 ml!")
        self.__water_needed = value

    @abstractmethod
    def plant_details(self):
        pass
