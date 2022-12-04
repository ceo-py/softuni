zoo = {"Area": {}}
data_input = input()

while data_input != "EndDay":

    command_, data = data_input.split(": ")

    if command_ == "Add":
        animal_name, needed_food_quantity, area = data.split("-")
        zoo[animal_name] = zoo.get(animal_name, 0) + int(needed_food_quantity)
        if area not in zoo["Area"]:
            zoo["Area"][area] = []
        if animal_name not in zoo["Area"][area]:
            zoo["Area"][area].append(animal_name)

    elif command_ == "Feed":
        animal_name, needed_food_quantity = data.split("-")
        if animal_name in zoo:
            zoo[animal_name] -= int(needed_food_quantity)
            if zoo[animal_name] <= 0:
                del zoo[animal_name]
                for pet_names in zoo["Area"].values():
                    if animal_name in pet_names:
                        pet_names.remove(animal_name)
                        break
                print(f"{animal_name} was successfully fed")

    data_input = input()

if zoo:
    print("Animals:")
    [print(f" {name} -> {quantity}g") for name, quantity in zoo.items() if name != "Area"]

if zoo["Area"]:
    print("Areas with hungry animals:")
    [print(f" {area_name}: {len(zoo['Area'][area_name])}") for area_name in zoo["Area"] if zoo["Area"][area_name]]




# zoo = {"Area": {}}
# data_input = input()
#
# while data_input != "EndDay":
#
#     command_, data = data_input.split(": ")
#
#     if command_ == "Add":
#         animal_name, needed_food_quantity, area = data.split("-")
#         zoo[animal_name] = zoo.get(animal_name, 0) + int(needed_food_quantity)
#         zoo["Area"][area] = zoo["Area"].get(area, []) + [animal_name]
#
#     elif command_ == "Feed":
#         animal_name, needed_food_quantity = data.split("-")
#         if animal_name in zoo:
#             zoo[animal_name] -= int(needed_food_quantity)
#             if zoo[animal_name] <= 0:
#                 del zoo[animal_name]
#                 for pet_names in zoo["Area"].values():
#                     while animal_name in pet_names:
#                         pet_names.remove(animal_name)
#                 print(f"{animal_name} was successfully fed")
#
#     data_input = input()
#
# if zoo:
#     print("Animals:")
#     [print(f" {name} -> {quantity}g") for name, quantity in zoo.items() if name != "Area"]
#
# if zoo["Area"]:
#     print("Areas with hungry animals:")
#     [print(f" {area_name}: {len(set(zoo['Area'][area_name]))}") for area_name in zoo["Area"] if zoo["Area"][area_name]]
#
#



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

#
# Examples
# Input	Output
# Add: Adam-4500-ByTheCreek
# Add: Maya-7600-WaterfallArea
# Add: Maya-1230-WaterfallArea
# Feed: Jamie-2000
# EndDay	Animals:
#  Adam -> 4500g
#  Maya -> 8830g
# Areas with hungry animals:
#  ByTheCreek: 1
#  WaterfallArea: 1
# Add: Jamie-600-WaterfallArea
# Add: Maya-6570-WaterfallArea
# Add: Adam-4500-ByTheCreek
# Add: Bobbie-6570-WaterfallArea
# Feed: Jamie-2000
# Feed: Adam-2000
# Feed: Adam-2500
# EndDay	Jamie was successfully fed
# Adam was successfully fed
# Animals:
#  Maya -> 6570g
#  Bobbie -> 6570g
# Areas with hungry animals:
#  WaterfallArea: 2
# Add: Bonie-3490-RiverArea
# Add: Sam-5430-DeepWoodsArea
# Add: Bonie-200-RiverArea
# Add: Maya-4560-ByTheCreek
# Feed: Maya-2390
# Feed: Bonie-3500
# Feed: Johny-3400
# Feed: Sam-5500
# EndDay	Sam was successfully fed
# Animals:
#  Bonie -> 190g
#  Maya -> 2170g
# Areas with hungry animals:
#  RiverArea: 1
#  ByTheCreek: 1