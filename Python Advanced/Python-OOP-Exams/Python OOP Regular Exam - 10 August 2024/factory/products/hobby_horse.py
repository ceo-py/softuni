from project.products.base_product import BaseProduct

class HobbyHorse(BaseProduct):
    DISCOUNT = 0.80

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material="Wood/Plastic", sub_type="Toys")

    def discount(self):
            self.price *= self.DISCOUNT