from project.clients.base_client import BaseClient

class BusinessClient(BaseClient):
    def __init__(self, name: str, phone_number: str):
        super().__init__(name, phone_number)

    def update_discount(self):
        self.discount = 10.0 if self.total_orders >= 2 else 0.0
