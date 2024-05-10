from abc import ABC, abstractmethod
from project.utils.validations import Validation


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_empty_string(value, "Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value: str):
        Validation.is_correct_type(
            value, ("VIP", "Regular"), "Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        if self.points >= 100:
            self.points -= 100
            return 10, self.points

        if self.points >= 50:
            self.points -= 50
            return 5, self.points

        return 0, self.points
