class Flower:
    def __init__(self, name,water_requirements):
        self.name = name
        self.water_requirements = int(water_requirements)
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"
