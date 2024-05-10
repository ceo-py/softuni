from abc import ABC, abstractmethod
from project.utils.validations import Validation


class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_number_in_range(
            len(value), 3, 50, "Waiter name must be between 3 and 50 characters in length!")
        self.__name = value

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value: str):
        Validation.is_number_under(
            value, 0, "Cannot have negative hours worked!")
        self.__hours_worked = value

    @abstractmethod
    def calculate_earnings(self):
        pass

    @abstractmethod
    def report_shift(self):
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"
