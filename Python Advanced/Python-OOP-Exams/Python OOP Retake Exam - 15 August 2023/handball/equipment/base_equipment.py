from abc import ABC, abstractmethod


class BaseEquipment(ABC):

    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abstractmethod
    def increase_price(self):
        pass
