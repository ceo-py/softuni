data_input = input()

animals_information = {}


class Animals:
    def __init__(self, type_animal, name, age, other):
        self.type_animal = type_animal
        self.name = name
        self.age = int(age)
        self.other = int(other)


class Dog(Animals):

    def produce_sound(self):
        return f"I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __repr__(self):
        return f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.other}"


class Cat(Animals):

    def produce_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __repr__(self):
        return f"Cat: {self.name}, Age: {self.age}, IQ: {self.other}"


class Snake(Animals):

    def produce_sound(self):
        return f"I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def __repr__(self):
        return f"Snake: {self.name}, Age: {self.age}, Cruelty: {self.other}"


while data_input != "I'm your Huckleberry":
    name, *info = data_input.split()
    if "Dog" == name:
        animals_information[info[0]] = Dog(name, *info)
    elif "Cat" == name:
        animals_information[info[0]] = Cat(name, *info)
    elif "Snake" == name:
        animals_information[info[0]] = Snake(name, *info)
    if name == "talk":
        print(animals_information[info[0]].produce_sound())
    data_input = input()

for animal in sorted(animals_information,
                     key=lambda x: (
                             animals_information[x].type_animal == "Snake", animals_information[x].type_animal == "Cat",
                             animals_information[x].type_animal == "Dog")):
    print(animals_information[animal])
