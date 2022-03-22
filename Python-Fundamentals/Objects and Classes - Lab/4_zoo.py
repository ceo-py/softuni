class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.name_zoo}: {', '.join(self.mammals)}\nTotal animals: {zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\nTotal animals: {zoo.__animals}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.name_zoo}: {', '.join(self.birds)}\nTotal animals: {zoo.__animals}"


zoo = Zoo(input())

for _ in range(int(input())):
    animal_type = input().split()
    zoo.add_animal(animal_type[0], animal_type[-1])

print(zoo.get_info(input()))
