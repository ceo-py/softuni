from abc import ABC, abstractmethod
from project.util.vd import Validation


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_empty_string(
            value, 'Team name cannot be empty!')
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: int):
        Validation.is_string_len_under(
            value, 2, 'Team country should be at least 2 symbols long!')
        self.__country = value
        

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value: str):
        Validation.is_number_under(
            value, 1, 'Advantage must be greater than zero!')
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def team_score(self):
        return self.advantage + sum(e.protection for e in self.equipment)

    def get_average_protection(self):
        sum = 0
        for equipment in self.equipment:
            sum += equipment.protection

        if not sum:
            return 0

        return int(sum / len(self.equipment))

    def get_statistics(self):
        output = [
            f'Name: {self.name}',
            f'Country: {self.country}',
            f'Advantage: {self.advantage} points',
            f'Budget: {self.budget:.2f}EUR',
            f'Wins: {self.wins}',
            f'Total Equipment Price: {sum(e.price for e in self.equipment):.2f}',
            f'Average Protection: {self.get_average_protection()}',
        ]
        return '\n'.join(output)
