from abc import ABC, abstractmethod

from project.utl.validation import Validation


class BasePeak(ABC):

    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: int):
        Validation.string_less_than_symbols(value, 2)
        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value: int):
        Validation.is_number_under(
            value, 1500, 'Peak elevation cannot be below 1500m.')
        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self):
        pass

    @abstractmethod
    def calculate_difficulty_level(self):
        pass
