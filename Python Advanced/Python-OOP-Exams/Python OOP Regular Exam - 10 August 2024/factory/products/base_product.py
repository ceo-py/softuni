from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        Validation.white_space_or_less_than_three_characters(
            value, "Product model must be at least 3 chars long!")
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: str):
        Validation.is_number_under(
            value, 0.01, "Product price must be greater than zero!")
        self.__price = value

    @abstractmethod
    def discount(self):
        pass
