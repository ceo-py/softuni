from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.alphanumeric_with_spaces(
            value, "Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value: str):
        Validation.is_number_equal_or_under(
            value, 0.0, "A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value: str):
        Validation.is_number_equal_or_under(
            value, 0, "A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        return self.available_money >= artifact_price and self.available_space >= artifact_space_required

    def __str__(self):
        output = [
            f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: {self.available_space}; Artifacts: "
        ]

        if not self.purchased_artifacts:
            output[-1] += "none"
        else:
            output[-1] += (", ".join(artifact.name for artifact in sorted(self.purchased_artifacts, key=lambda artifact: artifact.name, reverse=True)))    

        return "\n".join(output)
