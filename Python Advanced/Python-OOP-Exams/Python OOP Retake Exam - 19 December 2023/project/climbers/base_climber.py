from abc import ABC, abstractmethod

from project.peaks.base_peak import BasePeak
from project.utl.validation import Validation


class BaseClimber(ABC):

    def __init__(self,  name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list = []
        self.is_prepared: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_empty_string(
            value, 'Climber name cannot be null or empty!')
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value: str):
        Validation.is_number_under(
            value, 1, 'A climber cannot have negative strength or strength equal to 0!')
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self) -> None:
        self.strength += 15

    def sort_conquered_peaks(self):
        self.conquered_peaks.sort()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///"
