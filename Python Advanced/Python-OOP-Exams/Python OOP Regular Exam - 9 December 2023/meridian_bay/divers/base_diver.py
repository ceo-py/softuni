from abc import ABC, abstractmethod
from project.uti.vd import Validation
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_empty_string(
            value, 'Diver name cannot be null or empty!')
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: str):
        Validation.is_number_under(
            value, 0, 'Cannot create diver with negative oxygen level!')
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def is_oxygen_level_enough(self, decrease_by: int):
        if self.oxygen_level - decrease_by < 0:
            self.oxygen_level = 0
            self.has_health_issue = True
            return False
        return True

    def hit(self, fish: BaseFish):
        if self.is_oxygen_level_enough(fish.time_to_catch):
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += round(fish.points)

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f'{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]'
