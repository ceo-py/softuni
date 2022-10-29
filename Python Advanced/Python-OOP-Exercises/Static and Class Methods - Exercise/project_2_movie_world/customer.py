class Customer:

    def __init__(self, name, age, id):
        self.id = id
        self.age = age
        self.name = name
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} " \
               f"has {len(self.rented_dvds)} rented DVD's ({', '.join(x.name for x in self.rented_dvds)})"
