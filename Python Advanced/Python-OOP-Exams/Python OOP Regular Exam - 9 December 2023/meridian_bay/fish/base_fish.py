from abc import ABC, abstractmethod
from project.uti.vd import Validation


class BaseFish(ABC):

    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_empty_string(value, 'Fish name should be determined!')
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value: str):
        Validation.is_number_in_range(
            value, 1, 10, 'Points should be a value ranging from 1 to 10!')
        self.__points = value

    @abstractmethod
    def fish_details(self):
        pass
