from abc import ABC, abstractmethod

from project.validation.validation import Validation


class FormulaTeam(ABC):
    teams = {
        "Red Bull": {
            1: 1_520_000,
            2: 820_000,
            3: 20_000,
            4: 20_000,
            5: 20_000,
            6: 20_000,
            7: 20_000,
            8: 20_000,
            9: 10_000,
            10: 10_000,
        },
        "Mercedes": {
            1: 1_100_000,
            2: 600_000,
            3: 600_000,
            4: 100_000,
            5: 100_000,
            6: 50_000,
            7: 50_000,
        }
    }

    def __init__(self, budget: int) -> object:
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, value):
        Validation.less_than(value, 1_000_000, "F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass
