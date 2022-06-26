route = input().split("||")
starting_fuel = int(input())
starting_ammunitions = int(input())

abort_missing = False


def traver(light_years):
    global starting_fuel, abort_missing
    if starting_fuel >= light_years:
        starting_fuel -= light_years
        print(f"The spaceship travelled {light_years} light-years.")
    else:
        print("Mission failed.")
        abort_missing = True


def enemy(enemy_armor):
    global starting_ammunitions, starting_fuel, abort_missing
    if starting_ammunitions >= enemy_armor:
        starting_ammunitions -= enemy_armor
        print(f"An enemy with {enemy_armor} armour is defeated.")
    elif starting_fuel >= enemy_armor * 2:
        starting_fuel -= enemy_armor * 2
        print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
    else:
        print("Mission failed.")
        abort_missing = True


def repair(number):
    global starting_ammunitions, starting_fuel
    starting_fuel += number
    starting_ammunitions += (number * 2)
    print(f"Ammunitions added: {number * 2}.")
    print(f"Fuel added: {number}.")


def titan():
    print("You have reached Titan, all passengers are safe.")


for command in route:
    if "Titan" not in command:
        command_type, command_data = [int(x) if x.isdigit() else x for x in command.split()]
    else:
        titan()
        break
    if "Travel" in command_type:
        traver(command_data)
    elif "Enemy" in command_type:
        enemy(command_data)
    elif "Repair" in command_type:
        repair(command_data)
    if abort_missing:
        break
