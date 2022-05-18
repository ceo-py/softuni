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




# data_input = input()
#
# talk_info = {}
#
#
# class Dog:
#     dogs_collection = []
#
#     def __init__(self, name, age, legs):
#         self.name = name
#         self.age = int(age)
#         self.legs = int(legs)
#
#     @staticmethod
#     def produce_sound():
#         return f"I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
#
#
# class Cat:
#     cats_collection = []
#
#     def __init__(self, name, age, intelligence):
#         self.name = name
#         self.age = int(age)
#         self.intelligence = int(intelligence)
#
#     @staticmethod
#     def produce_sound():
#         return f"I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
#
#
# class Snake:
#     snake_collection = []
#
#     def __init__(self, name, age, cruelty):
#         self.name = name
#         self.age = int(age)
#         self.cruelty = int(cruelty)
#
#     @staticmethod
#     def produce_sound():
#         return f"I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
#
#
# while data_input != "I'm your Huckleberry":
#     name, *info = data_input.split()
#     if "Dog" == name:
#         Dog.dogs_collection.append(Dog(*info))
#         talk_info[info[0]] = Dog.produce_sound()
#     elif "Cat" == name:
#         Cat.cats_collection.append(Cat(*info))
#         talk_info[info[0]] = Cat.produce_sound()
#     elif "Snake" == name:
#         Snake.snake_collection.append(Snake(*info))
#         talk_info[info[0]] = Snake.produce_sound()
#     if name == "talk":
#         print(talk_info[info[0]])
#     data_input = input()
#
# for show in Dog.dogs_collection:
#     print(f"Dog: {show.name}, Age: {show.age}, Number Of Legs: {show.legs}")
# for show in Cat.cats_collection:
#     print(f"Cat: {show.name}, Age: {show.age}, IQ: {show.intelligence}")
# for show in Snake.snake_collection:
#     print(f"Snake: {show.name}, Age: {show.age}, Cruelty: {show.cruelty}")


# data_input = input()
#
#


# class Dog:
#     talk_info = {}
#     dogs_collection = []
#
#     def __init__(self, name, age, legs):
#         self.name = name
#         self.age = int(age)
#         self.legs = int(legs)
#
#     @staticmethod
#     def produce_sound():
#         return f"I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
#
#
# class Cat:
#     cats_collection = []
#
#     def __init__(self, name, age, intelligence):
#         self.name = name
#         self.age = int(age)
#         self.intelligence = int(intelligence)
#
#     @staticmethod
#     def produce_sound():
#         return f"I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
#
#
# class Snake:
#     snake_collection = []
#
#     def __init__(self, name, age, cruelty):
#         self.name = name
#         self.age = int(age)
#         self.cruelty = int(cruelty)
#
#     @staticmethod
#     def produce_sound():
#         return f"I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
#
#
# while data_input != "I'm your Huckleberry":
#     name, *info = data_input.split()
#     if "Dog" == name:
#         Dog.dogs_collection.append(Dog(*info))
#         Dog.talk_info[info[0]] = Dog.produce_sound()
#     elif "Cat" == name:
#         Cat.cats_collection.append(Cat(*info))
#         Dog.talk_info[info[0]] = Cat.produce_sound()
#     elif "Snake" == name:
#         Snake.snake_collection.append(Snake(*info))
#         Dog.talk_info[info[0]] = Snake.produce_sound()
#     if name == "talk":
#         if info[0] in list(map(lambda ap: ap.name, Dog.dogs_collection)):
#             print(Dog.produce_sound())
#         if info[0] in list(map(lambda ap: ap.name, Cat.cats_collection)):
#             print(Cat.produce_sound())
#         elif info[0] in list(map(lambda ap: ap.name, Snake.snake_collection)):
#             print(Snake.produce_sound())
#
#     data_input = input()
#
#
# for show in Dog.dogs_collection:
#     print(f"Dog: {show.name}, Age: {show.age}, Number Of Legs: {show.legs}")
# for show in Cat.cats_collection:
#     print(f"Cat: {show.name}, Age: {show.age}, IQ: {show.intelligence}")
# for show in Snake.snake_collection:
#     print(f"Snake: {show.name}, Age: {show.age}, Cruelty: {show.cruelty}")
#
#
