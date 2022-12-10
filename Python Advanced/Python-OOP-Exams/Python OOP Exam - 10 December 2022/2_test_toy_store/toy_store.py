class ToyStore:
    def __init__(self):
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def add_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")
        if self.toy_shelf[shelf] == toy_name:
            raise Exception("Toy is already in shelf!")
        if self.toy_shelf[shelf] is not None:
            raise Exception("Shelf is already taken!")
        self.toy_shelf[shelf] = toy_name
        return f"Toy:{toy_name} placed successfully!"

    def remove_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")
        if self.toy_shelf[shelf] != toy_name:
            raise Exception("Toy in that shelf doesn't exists!")
        self.toy_shelf[shelf] = None
        return f"Remove toy:{toy_name} successfully!"
