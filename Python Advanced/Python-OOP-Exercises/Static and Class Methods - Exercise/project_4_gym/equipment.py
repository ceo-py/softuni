class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        result = Equipment.id
        Equipment.id += 1
        return result

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
