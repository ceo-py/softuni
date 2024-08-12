from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore
from project.products.base_product import BaseProduct
from project.products.hobby_horse import HobbyHorse
from project.products.chair import Chair
from project.utils.validation import Validation


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products = []
        self.stores = []

    @property
    def product_types(self):
        return {
            "HobbyHorse": HobbyHorse,
            "Chair": Chair
        }

    @property
    def store_types(self):
        return {
            "FurnitureStore": FurnitureStore,
            "ToyStore": ToyStore
        }

    def _find_store(self, store_name: str) -> BaseStore:
        for store in self.stores:
            if store.name == store_name:
                return store

    def produce_item(self, product_type: str, model: str, price: float):
        Validation.valid_types(
            product_type, self.product_types, "Invalid product type!")
        product = self.product_types[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        Validation.valid_types(store_type, self.store_types,
                               f"{store_type} is an invalid type of store!")
        store = self.store_types[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [
            p for p in products if p.sub_type.lower() in store.store_type.lower()]
        if not filtered_products:
            return "Products do not match in type. Nothing sold."

        for product in filtered_products:
            self.products.remove(product)

            store.products.append(product)
            store.capacity -= 1
            self.income += product.price

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        Validation.store_with_name_exists(
            store_name, self.stores, "No such store!")

        store = self._find_store(store_name)

        if len(store.products) != 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        find_product = [p.discount()
                        for p in self.products if p.model == product_model]

        return f"Discount applied to {len(find_product)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self._find_store(store_name)

        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        products_unsold = {}
        for p in self.products:
            products_unsold[p.model] = products_unsold.get(p.model, 0) + 1

        output = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}",
            *[f"{product_model}: {count_}" for product_model,
                count_ in sorted(products_unsold.items(), key=lambda x: x[0])],
            f"***Partner Stores: {len(self.stores)}***",
            *sorted(s.name for s in (self.stores)),
        ]

        return "\n".join(output)


# Initialize the FactoryManager
factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store(
    "FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))
