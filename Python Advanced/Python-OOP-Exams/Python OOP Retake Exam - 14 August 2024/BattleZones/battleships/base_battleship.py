from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking = False
        self.is_available = True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_all_letters(
            value, "Ship name must contain only letters!")
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        if value < 0:
            value = 0
        # self.__health = max(value, 0)
        self.__health = value

    def take_damage(self, enemy_battleship):
        self.health -= enemy_battleship.hit_strength
    
    @abstractmethod
    def attack(self):
        pass
