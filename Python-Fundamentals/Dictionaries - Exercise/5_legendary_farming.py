items_information = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
shadowmourne = False
valanyr = False
dragonwrath = False


def check_from_items():
    global shadowmourne
    global valanyr
    global dragonwrath
    if items_information["shards"] >= 250:
        shadowmourne = True
        print(f"Shadowmourne obtained!")
        items_information["shards"] += - 250

    elif items_information["fragments"] >= 250:
        items_information["fragments"] += -250
        print(f"Valanyr obtained!")
        valanyr = True

    elif items_information["motes"] >= 250:
        items_information["motes"] += - 250
        print(f"Dragonwrath obtained!")
        dragonwrath = True


def print_winner():
    for key, value in items_information.items():
        print(f"{key}: {value}")


while not shadowmourne and not valanyr and not dragonwrath:
    collected_items = input().lower().split()
    i = 1
    counter = 0
    for _ in range(int(len(collected_items) / 2)):
        type_item = collected_items[i]
        quantity_item = int(collected_items[counter])
        items_information[collected_items[i]] = items_information.get(collected_items[i], 0)
        items_information[type_item] += quantity_item
        counter += 2
        i += 2
        check_from_items()
        if shadowmourne or valanyr or dragonwrath:
            break

print_winner()
