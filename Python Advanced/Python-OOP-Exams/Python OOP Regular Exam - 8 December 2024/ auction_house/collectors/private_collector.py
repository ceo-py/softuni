from project.collectors.base_collector import BaseCollector

class PrivateCollector(BaseCollector):
    AVAILABLE_MONEY = 25_000.0
    AVAILABLE_SPACE = 3_000
    MONEY_INCREASE_AMOUNT = 5000.0

    def __init__(self, name: str):
        super().__init__(name, available_money=PrivateCollector.AVAILABLE_MONEY, available_space=PrivateCollector.AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += PrivateCollector.MONEY_INCREASE_AMOUNT