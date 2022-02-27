dragons = int(input())

dragon_information = {}


def create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
    if dragon_type not in dragon_information:
        dragon_information[dragon_type] = {}
    if dragon_name not in dragon_information[dragon_type]:
        dragon_information[dragon_type][dragon_name] = {}
        dragon_information[dragon_type][dragon_name]["damage"] = dragon_damage
        dragon_information[dragon_type][dragon_name]["health"] = dragon_health
        dragon_information[dragon_type][dragon_name]["armor"] = dragon_armor
    dragon_information[dragon_type][dragon_name]["damage"] = dragon_damage
    dragon_information[dragon_type][dragon_name]["health"] = dragon_health
    dragon_information[dragon_type][dragon_name]["armor"] = dragon_armor


def show_result():
    damage_d = "damage"
    health_d = "health"
    armor_d = "armor"
    for color in dragon_information:
        i = 0
        damage = 0
        health = 0
        armor = 0
        for name in dragon_information[color]:
            damage += dragon_information[color][name]["damage"]
            health += dragon_information[color][name]["health"]
            armor += dragon_information[color][name]["armor"]
            i += 1
        print(f"{color}::({(damage / i):.2f}/{(health / i):.2f}/{(armor / i):.2f})")
        for name in sorted(dragon_information[color].keys()):
            print(
                f"-{name} -> damage: {dragon_information[color][name][damage_d]}, health: {dragon_information[color][name][health_d]}, armor: {dragon_information[color][name][armor_d]}")


for _ in range(dragons):
    command = input()
    command = command.split()
    dragon_type = command[0]
    dragon_name = command[1]
    if (command[2]) == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(command[2])
    if (command[3]) == "null":
        dragon_health = 250
    else:
        dragon_health = int(command[3])
    if (command[4]) == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(command[4])

    create_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)


show_result()
