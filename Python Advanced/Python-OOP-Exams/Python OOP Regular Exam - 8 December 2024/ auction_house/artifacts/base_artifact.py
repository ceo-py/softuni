from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseArtifact(ABC):
    def __init__(self, name: str, price: float, space_required: int):
        self.name = name
        self.price = price
        self.space_required = space_required

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.empty_string_or_empty_spaces(
            value, "Artifact name cannot be null or empty!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        Validation.is_number_equal_or_under(
            value, 0.0, "Artifact price should be more than 0.0!")
        self.__price = value

    @property
    def space_required(self):
        return self.__space_required

    @space_required.setter
    def space_required(self, value: int):
        Validation.is_number_in_range_of_two_numbers(
            value, 1, 1000, "Space required for the artifact exhibition must be between 1 and 1000!")
        self.__space_required = value

    @abstractmethod
    def artifact_information(self):
        pass
