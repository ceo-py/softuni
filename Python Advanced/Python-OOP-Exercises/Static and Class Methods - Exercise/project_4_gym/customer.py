class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.address = address
        self.email = email
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        result = Customer.id
        Customer.id += 1
        return result

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
