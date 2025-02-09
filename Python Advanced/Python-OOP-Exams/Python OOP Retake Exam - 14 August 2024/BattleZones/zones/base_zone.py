from abc import ABC, abstractmethod
from project.utils.validation import Validation


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships = []


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        Validation.is_all_digits(
            value, "Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda x: (-x.hit_strength, x.name))

    def get_royal_and_pirate_ships(self) -> tuple:
        royal_ships = []
        pirates_ships = []
        for ship in self.ships:
            target_ship = royal_ships if ship.__class__.__name__ == "RoyalBattleship" else pirates_ships
            target_ship.append(ship)

        return royal_ships, pirates_ships

    @abstractmethod
    def zone_info(self):
        pass
