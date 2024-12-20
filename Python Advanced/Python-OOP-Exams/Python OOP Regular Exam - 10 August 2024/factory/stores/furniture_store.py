from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        count_products = {}
        for p in (self.products):
            count_products[p.model] = count_products.get(p.model, []) + [p]

        sorted_models = dict(
            sorted(count_products.items(), key=lambda items: items[0]))

        output = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Furniture for sale:",
            *[f"{model_name}: {len(models)}pcs, average price: {sum(m.price for m in models) / len(models):.2f}" for model_name, models in sorted_models.items()]
        ]

        return "\n".join(output)