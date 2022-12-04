
zoo = {}
data_input = input()

while data_input != "EndDay":

    command_, data = data_input.split(": ")

    if command_ == "Add":
        animal_name, needed_food_quantity, area = data.split("-")
        zoo[animal_name] = zoo.get(animal_name, 0) + int(needed_food_quantity)
        zoo["Area"] = zoo["Area"].get(area, []) + [animal_name]

    elif command_ == "Feed":
        animal_name, needed_food_quantity = data.split("-")
        if animal_name in zoo:
            zoo[animal_name] -= int(needed_food_quantity)
            if zoo[animal_name] <= 0:
                del zoo[animal_name]
                for pet_names in zoo["Area"].values():
                    if animal_name in pet_names:
                        pet_names.remove(animal_name)
                print(f"{animal_name} was successfully fed")

    data_input = input()

if zoo:
    print("Animals:")
    [print(f"{name} -> {quantity}g") for name, quantity in zoo.items() if name != "Area"]

if zoo["Area"]:
    print("Areas with hungry animals:")
    [print(f"{area_name}: {len(set(zoo['Area'][area_name]))}") for area_name in zoo["Area"] if zoo["Area"][area_name]]








# zoo = {}
# area = {}
# data_input = input()
#
# while data_input != "EndDay":
#
#     command_, data = data_input.split(": ")
#
#     if command_ == "Add":
#         animal_name, needed_food_quantity, area_input = data.split("-")
#         zoo[animal_name] = zoo.get(animal_name, 0) + int(needed_food_quantity)
#         area[area_input] = area.get(area_input, []) + [animal_name]
#
#     elif command_ == "Feed":
#         animal_name, needed_food_quantity = data.split("-")
#         if animal_name in zoo:
#             zoo[animal_name] -= int(needed_food_quantity)
#             if zoo[animal_name] <= 0:
#                 del zoo[animal_name]
#                 for pet_names in area.values():
#                     if animal_name in pet_names:
#                         pet_names.remove(animal_name)
#                 print(f"{animal_name} was successfully fed")
#
#     data_input = input()
#
# if zoo:
#     print("Animals:")
#     [print(f"{name} -> {quantity}g") for name, quantity in zoo.items()]
#
# if area:
#     print("Areas with hungry animals:")
#     [print(f"{area_name}: {len(set(area[area_name]))}") for area_name in area if area[area_name]]
#
#
#
#
