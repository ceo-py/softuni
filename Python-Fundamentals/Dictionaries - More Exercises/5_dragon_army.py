dragons = int(input())

dragon_information = {}
damage_d, health_d, armor_d = "damage", "health", "armor"


def create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
    dragon_information[dragon_type] = dragon_information.get(dragon_type, dict())
    dragon_information[dragon_type][dragon_name] = dragon_information.get(dragon_name, dict())
    dragon_information[dragon_type][dragon_name][damage_d] = dragon_damage
    dragon_information[dragon_type][dragon_name][health_d] = dragon_health
    dragon_information[dragon_type][dragon_name][armor_d] = dragon_armor


def show_result():
    for color in dragon_information:
        damage, health, armor = 0, 0, 0
        for name in dragon_information[color]:
            damage += dragon_information[color][name][damage_d]
            health += dragon_information[color][name][health_d]
            armor += dragon_information[color][name][armor_d]
        total_dragons = len(dragon_information[color])
        print(f"{color}::({(damage / total_dragons):.2f}/{(health / total_dragons):.2f}/{(armor / total_dragons):.2f})")
        for name in sorted(dragon_information[color].keys()):
            print(
                f"-{name} -> damage: {dragon_information[color][name][damage_d]}, health: {dragon_information[color][name][health_d]}, armor: {dragon_information[color][name][armor_d]}")


for _ in range(dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()
    if damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == "null":
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(armor)
    create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

show_result()





# number_of_dragons = int(input())
# dragons_by_colours = {}
#
# for _ in range(number_of_dragons):
#     colour, name, damage, health, armor = (int(x) if x.isdigit() else x for x in input().split())
#     dragons_by_colours[colour] = dragons_by_colours.get(colour, {})
#     dragons_by_colours[colour][name] = (45 if damage == "null" else damage,
#                                         250 if health == "null" else health,
#                                         10 if armor == "null" else armor)
#
# average_per_colour = {}
# for colour, name in dragons_by_colours.items():
#     avg_for_color = []
#     for dragon, info in name.items():
#         avg_for_color.append(info)
#         avg_result = [sum(i) / len(avg_for_color) for i in zip(*avg_for_color)]
#     average_per_colour[colour] = avg_result
#
# sorted_dictionary = {k: {x: y for x, y in sorted(v.items())} for k, v in dragons_by_colours.items()}
#
# for colour, data in average_per_colour.items():
#     print(f"{colour}::({'/'.join(f'{x:.2f}' for x in data)})")
#     for name, data in sorted_dictionary[colour].items():
#         print(f"-{name} -> {', '.join(f'{x}: {y}' for x, y in zip(('damage', 'health', 'armor'), data))}")




# number_of_dragons = int(input())
# dragons_by_colours = {}
#
# for _ in range(number_of_dragons):
#     colour, name, damage, health, armor = input().split()
#     if colour not in dragons_by_colours:
#         dragons_by_colours[colour] = {}
#     if damage == "null":
#         dragon_damage = 45
#     else:
#         dragon_damage = int(damage)
#     if health == "null":
#         dragon_health = 250
#     else:
#         dragon_health = int(health)
#     if armor == "null":
#         dragon_armor = 10
#     else:
#         dragon_armor = int(armor)
#     dragons_by_colours[colour][name] = [dragon_damage, dragon_health, dragon_armor]
#
# average_per_colour = {}
# for colour, name in dragons_by_colours.items():
#     avg_for_colour = []
#     for dragon, info in name.items():
#         if len(name) > 1:
#             avg_for_colour.append(info)
#         else:
#             avg_for_colour.append(info)
#         avg_result = [sum(i) / len(avg_for_colour) for i in zip(*avg_for_colour)]
#     average_per_colour[colour] = avg_result
#
# sorted_dictionary = {k: {x: y for x, y in sorted(v.items())} for k, v in dragons_by_colours.items()}
#
# for colour, average in average_per_colour.items():
#     print(f"{colour}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})")
#     for name, info in sorted_dictionary[colour].items():
#         print(f"-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")
#




#
# dragons = int(input())
#
# dragon_information = {}
# damage_d = "damage"
# health_d = "health"
# armor_d = "armor"
#
#
# def create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
#     if dragon_type not in dragon_information:
#         dragon_information[dragon_type] = {}
#     if dragon_name not in dragon_information[dragon_type]:
#         dragon_information[dragon_type][dragon_name] = {}
#     dragon_information[dragon_type][dragon_name][damage_d] = dragon_damage
#     dragon_information[dragon_type][dragon_name][health_d] = dragon_health
#     dragon_information[dragon_type][dragon_name][armor_d] = dragon_armor
#
#
# def show_result():
#     for color in dragon_information:
#         damage = 0
#         health = 0
#         armor = 0
#         for name in dragon_information[color]:
#             damage += dragon_information[color][name][damage_d]
#             health += dragon_information[color][name][health_d]
#             armor += dragon_information[color][name][armor_d]
#         total_dragons = len(dragon_information[color])
#         print(f"{color}::({(damage / total_dragons):.2f}/{(health / total_dragons):.2f}/{(armor / total_dragons):.2f})")
#         for name in sorted(dragon_information[color].keys()):
#             print(
#                 f"-{name} -> damage: {dragon_information[color][name][damage_d]}, health: {dragon_information[color][name][health_d]}, armor: {dragon_information[color][name][armor_d]}")
#
#
# for _ in range(dragons):
#     command = input()
#     command = command.split()
#     dragon_type = command[0]
#     dragon_name = command[1]
#     if (command[2]) == "null":
#         dragon_damage = 45
#     else:
#         dragon_damage = int(command[2])
#     if (command[3]) == "null":
#         dragon_health = 250
#     else:
#         dragon_health = int(command[3])
#     if (command[4]) == "null":
#         dragon_armor = 10
#     else:
#         dragon_armor = int(command[4])
#
#     create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)
#
# show_result()



#
# dragons = int(input())
#
# dragon_information = {}
#
#
# def create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
#     if dragon_type not in dragon_information:
#         dragon_information[dragon_type] = {}
#     if dragon_name not in dragon_information[dragon_type]:
#         dragon_information[dragon_type][dragon_name] = {}
#         dragon_information[dragon_type][dragon_name]["damage"] = dragon_damage
#         dragon_information[dragon_type][dragon_name]["health"] = dragon_health
#         dragon_information[dragon_type][dragon_name]["armor"] = dragon_armor
#     dragon_information[dragon_type][dragon_name]["damage"] = dragon_damage
#     dragon_information[dragon_type][dragon_name]["health"] = dragon_health
#     dragon_information[dragon_type][dragon_name]["armor"] = dragon_armor
#
#
# def show_result():
#     damage_d = "damage"
#     health_d = "health"
#     armor_d = "armor"
#     for color in dragon_information:
#         i = 0
#         damage = 0
#         health = 0
#         armor = 0
#         for name in dragon_information[color]:
#             damage += dragon_information[color][name]["damage"]
#             health += dragon_information[color][name]["health"]
#             armor += dragon_information[color][name]["armor"]
#             i += 1
#         print(f"{color}::({(damage / i):.2f}/{(health / i):.2f}/{(armor / i):.2f})")
#         for name in sorted(dragon_information[color].keys()):
#             print(
#                 f"-{name} -> damage: {dragon_information[color][name][damage_d]}, health: {dragon_information[color][name][health_d]}, armor: {dragon_information[color][name][armor_d]}")
#
#
# for _ in range(dragons):
#     command = input()
#     command = command.split()
#     dragon_type = command[0]
#     dragon_name = command[1]
#     if (command[2]) == "null":
#         dragon_damage = 45
#     else:
#         dragon_damage = int(command[2])
#     if (command[3]) == "null":
#         dragon_health = 250
#     else:
#         dragon_health = int(command[3])
#     if (command[4]) == "null":
#         dragon_armor = 10
#     else:
#         dragon_armor = int(command[4])
#
#     create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)
#
#
# show_result()
