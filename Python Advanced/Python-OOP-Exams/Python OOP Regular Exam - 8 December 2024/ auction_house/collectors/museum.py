from project.collectors.base_collector import BaseCollector

class Museum(BaseCollector):
    AVAILABLE_MONEY = 15_000.0
    AVAILABLE_SPACE = 2_000
    MONEY_INCREASE_AMOUNT = 1000.0

    def __init__(self, name: str):
        super().__init__(name, available_money=Museum.AVAILABLE_MONEY, available_space=Museum.AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += Museum.MONEY_INCREASE_AMOUNT