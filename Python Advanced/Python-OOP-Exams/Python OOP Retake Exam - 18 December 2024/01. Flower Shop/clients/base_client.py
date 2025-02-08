from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseClient(ABC):
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.discount = 0.0
        self.total_orders = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_name_two_char(
            value, 2, "Name must be at least two characters long!")
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        Validation.is_only_digits(
            value, "Phone number can contain only digits!")
        self.__phone_number = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self):
        return f"Client: {self.name}, Phone number: {self.phone_number}, Orders count: {self.total_orders}, Discount: {int(self.discount)}%"
