animals_info = []
name_animal = {"mammal": "Mammals", "fish": "Fishes", "bird": "Birds"}


class Zoo:
    __animals = 0

    def __init__(self, name_zoo, name, type):
        self.name_zoo = name_zoo
        self.name = name
        self.type = type

    def get_info(self, species):
        if species == self.type:
            return True
        return False


zoo_name = input()
Zoo.animals = int(input())
for _ in range(Zoo.animals):
    type, name = input().split()
    animals_info.append(Zoo(zoo_name, name, type))

show_animals = input()
print(
    f"{name_animal[show_animals]} in {zoo_name}: {', '.join([x.name for x in animals_info if x.get_info(show_animals)])}")
print(f"Total animals: {Zoo.animals}")




# class Zoo:
#     __animals = 0
#
#     def __init__(self, name_zoo):
#         self.name_zoo = name_zoo
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#         zoo.__animals += 1
#
#     def get_info(self, species):
#         if species == "mammal":
#             return f"{species.capitalize()}s in {self.name_zoo}: {', '.join(self.mammals)}\nTotal animals: {zoo.__animals}"
#         elif species == "fish":
#             return f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\nTotal animals: {zoo.__animals}"
#         elif species == "bird":
#             return f"{species.capitalize()}s in {self.name_zoo}: {', '.join(self.birds)}\nTotal animals: {zoo.__animals}"
#
#
# zoo = Zoo(input())
#
# for _ in range(int(input())):
#     animal_type = input().split()
#     zoo.add_animal(animal_type[0], animal_type[-1])
#
# print(zoo.get_info(input()))
