class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.get_next_id()

    @staticmethod
    def get_next_id():
        result = Trainer.id
        Trainer.id += 1
        return result

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

