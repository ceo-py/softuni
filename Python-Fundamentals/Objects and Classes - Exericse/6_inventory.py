class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = int(capacity)
        self.items = []
        self.left_over = 0

    def add_item(self, item: str):
        if self.left_over < self.__capacity:
            self.items.append(str(item))
            self.left_over += 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.get_capacity(self) - self.left_over}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
