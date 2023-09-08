given_items = []

while True:
    try:
        original_list = input().split()
        [given_items.append([original_list[i], original_list[i + 1].lower()]) for i in range(0, len(original_list), 2)]
    except:
        break

collected_items = {
        'shards': 0,
        'fragments': 0,
        'motes': 0
}
collected_item_name = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'
}

for quantity, item in given_items:
    collected_items[item] = collected_items.get(item, 0) + int(quantity)

    if item in collected_item_name:
        found = False

        for collected_item, collected_quantity in list(collected_items.items())[:3]:
            if collected_quantity >= 250:
                collected_items[collected_item] -= 250
                print(f"{collected_item_name[collected_item]} obtained!")
                found = True
                break

        if found:
            break

for item, quantity in collected_items.items():
        print(f"{item}: {quantity}")





# items_information = {
#     "shards": 0,
#     "fragments": 0,
#     "motes": 0
# }
# shadowmourne = False
# valanyr = False
# dragonwrath = False
#
#
# def check_from_items():
#     global shadowmourne
#     global valanyr
#     global dragonwrath
#     if items_information["shards"] >= 250:
#         shadowmourne = True
#         print(f"Shadowmourne obtained!")
#         items_information["shards"] += - 250
#
#     elif items_information["fragments"] >= 250:
#         items_information["fragments"] += -250
#         print(f"Valanyr obtained!")
#         valanyr = True
#
#     elif items_information["motes"] >= 250:
#         items_information["motes"] += - 250
#         print(f"Dragonwrath obtained!")
#         dragonwrath = True
#
#
# def print_winner():
#     for key, value in items_information.items():
#         print(f"{key}: {value}")
#
#
# while not shadowmourne and not valanyr and not dragonwrath:
#     collected_items = input().lower().split()
#     i = 1
#     counter = 0
#     for _ in range(int(len(collected_items) / 2)):
#         type_item = collected_items[i]
#         quantity_item = int(collected_items[counter])
#         items_information[collected_items[i]] = items_information.get(collected_items[i], 0)
#         items_information[type_item] += quantity_item
#         counter += 2
#         i += 2
#         check_from_items()
#         if shadowmourne or valanyr or dragonwrath:
#             break
#
# print_winner()














# key_materials = {
#     "shards": ["Shadowmourne", 0],
#     "fragments": ["Valanyr" , 0],
#     "motes": ["Dragonwrath", 0 ]
# }
#
# junk_materials = {}
# all_materials =[]
#
# while True:
#     try:
#         all_materials += [int(x) if x.isdigit() else x.lower() for x in input().split()]
#     except:
#         break
#
# for i in range(0, len(all_materials), 2):
#     quantity = all_materials[i]
#     material = all_materials[i + 1]
#     if material in key_materials.keys():
#         key_materials[material][1] += quantity
#         if key_materials[material][1] >= 250:
#             key_materials[material][1] -= 250
#             print(f"{key_materials[material][0]} obtained!")
#             break
#     else:
#         junk_materials[material] = junk_materials.get(material, 0) + quantity
#
#
# for key, value in key_materials.items():
#     alabala = key_materials[key][1]
#     print(f"{key}: {alabala}")
# for k, v in junk_materials.items():
#     print(f"{k}: {v}")