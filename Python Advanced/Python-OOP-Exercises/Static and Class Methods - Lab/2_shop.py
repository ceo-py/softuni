class Shop:

    def __init__(self, name, type, capacity):
        self.capacity = capacity
        self.type = type
        self.name = name
        self.items = {}

    @staticmethod
    def small_shop(name: str, type: str):
        return Shop(name, type, 10)

    def add_item(self, item_name:str):
        if self.capacity > sum(self.items.values()):
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name:str, amount:int):
        if item_name not in self.items or self.items[item_name] - amount < 0:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] <= 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


