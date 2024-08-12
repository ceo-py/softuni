from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.empty_string_or_empty_spaces(
            value, "Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value: str):
        Validation.exact_three_characters(
            value, "Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: str):
        Validation.is_number_under(
            value, 0, "Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        profit = sum(product.price for product in self.products) * 0.10
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass
