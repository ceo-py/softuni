from project.utils.validation import Validation
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from project.clients.regular_client import RegularClient
from project.clients.business_client import BusinessClient

class FlowerShopManager:

    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []


    def get_valid_flower_type(self, flower_type: str):
        return {
            "Flower": Flower,
            "LeafPlant": LeafPlant
        }.get(flower_type)

    def get_valid_client_type(self, client_type: str):
        return {
            "RegularClient": RegularClient,
            "BusinessClient": BusinessClient
        }.get(client_type)

    def __find_object_by_attribute(self, text: str, attribute: str, collection: list) -> object:
        for obj in collection:
            if getattr(obj, attribute) == text:
                return obj

    def __find_multiply_objects_by_attribute(self, text: str, attribute: str, collection: list, limit: int) -> object:
        found_objects = []
        for obj in collection:
            if getattr(obj, attribute) == text:
                found_objects.append(obj)
            if len(found_objects) == limit:
                    break
        return found_objects

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        found_plant_type = self.get_valid_flower_type(plant_type)
        if not found_plant_type:
            raise ValueError("Unknown plant type!")

        new_plant = found_plant_type(plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        found_client_type = self.get_valid_client_type(client_type)
        if not found_client_type:
            raise ValueError("Unknown client type!")
        
        Validation.duplicate_attribute(client_phone_number, "phone_number", self.clients, "This phone number has been used!")
        new_client = found_client_type(client_name, client_phone_number)
        self.clients.append(new_client)

        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        found_client = self.__find_object_by_attribute(client_phone_number, "phone_number", self.clients)
        if not found_client:
            raise ValueError("Client not found!")

        found_plants = self.__find_multiply_objects_by_attribute(plant_name, "name", self.plants, plant_quantity)
        if not found_plants:
            raise ValueError("Plants not found!")

        if len(found_plants) < plant_quantity:
            return "Not enough plant quantity."

        [self.plants.remove(plant) for plant in found_plants]
        order_amount = (found_plants[-1].price * plant_quantity) * ((100 - found_client.discount) / 100)
        self.income += order_amount
        found_client.update_total_orders()
        found_client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

        
    def remove_plant(self, plant_name: str):
        found_plant = self.__find_object_by_attribute(plant_name, "name", self.plants)
        if not found_plant:
            return "No such plant name."

        self.plants.remove(found_plant)

        return f"Removed {found_plant.plant_details()}"
        

    def remove_clients(self):
        clients_with_zero_orders = [client for client in self.clients if client.total_orders == 0]
        [self.clients.remove(client) for client in clients_with_zero_orders]
        return f"{len(clients_with_zero_orders)} client/s removed."

    def shop_report(self):
        count_of_all_orders = sum(client.total_orders for client in self.clients)
        unsold_plants = {}
        for plant in self.plants:
            unsold_plants[plant.name] = unsold_plants.get(plant.name, 0) + 1
        output = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {count_of_all_orders}",
            f"~~Unsold plants: {len(self.plants)}~~",
            *[
                f"{name}: {count}" for name, count in sorted(unsold_plants.items(), key=lambda x: (-x[1], x[0]))
            ],
            f"~~Clients number: {len(self.clients)}~~",
            *(client.client_details() for client in sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number)))
        ]

        return "\n".join(output)











# Create an instance of FlowerShopManager
manager = FlowerShopManager()

# Add plants
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Lily", 20.00, 180, "Summer"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print()

# Add clients
print(manager.add_client("RegularClient", "Alice Johnson", "1234567890"))
print(manager.add_client("RegularClient", "Bob Smith", "0987654321"))
print(manager.add_client("BusinessClient", "Greenhouse Inc.", "5647382910"))
print(manager.add_client("BusinessClient", "CoolGarden Plc.", "9647382910"))
print(manager.add_client("RegularClient", "Peter Johnson", "382910"))
print()

# Perform sales
print(manager.sell_plants("1234567890", "Rose", 3))
print(manager.sell_plants("0987654321", "Tulip", 2))
print(manager.sell_plants("5647382910", "Cactus", 1))
print()

# Get shop report
print(manager.shop_report())
print()

# Perform sales
print(manager.sell_plants("1234567890", "Lily", 2))
print(manager.sell_plants("0987654321", "Fern", 1))
print(manager.sell_plants("5647382910", "Snake Plant", 2))
print()

# Remove a plant
print(manager.remove_plant("Nonexistent"))
print(manager.remove_plant("Cactus"))
print()

# Get shop report
print(manager.shop_report())
print()

# Remove clients who have no orders
print(manager.remove_clients())
print(manager.remove_clients())