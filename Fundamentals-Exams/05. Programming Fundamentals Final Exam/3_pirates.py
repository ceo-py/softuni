command = input()

population_d = "population"
cities_d = "cities"
gold_d = "gold"

town_info = {}

while command != "Sail":
    command = command.split("||")
    name_town = command[0]
    people_town = int(command[1])
    gold_town = int(command[-1])
    if name_town not in town_info:
        town_info[name_town] = {}
        town_info[name_town][population_d] = 0
        town_info[name_town][gold_d] = 0
    town_info[name_town][population_d] += people_town
    town_info[name_town][gold_d] += gold_town
    command = input()

event_command = input()

while event_command != "End":
    event_command = event_command.split("=>")
    type_command = event_command[0]
    name_town = event_command[1]
    people_town = int(event_command[2])
    if type_command == "Plunder":
        gold_town = int(event_command[-1])
        town_info[name_town][gold_d] -= gold_town
        town_info[name_town][population_d] -= people_town
        print(f"{name_town} plundered! {gold_town} gold stolen, {people_town} citizens killed.")
        if any([town_info[name_town][gold_d] <= 0, town_info[name_town][population_d] <= 0]):
            print(f"{name_town} has been wiped off the map!")
            del town_info[name_town]
    elif type_command == "Prosper":
        if people_town >= 0:
            town_info[name_town][gold_d] += people_town
            print(
                f"{people_town} gold added to the city treasury. {name_town} now has {town_info[name_town][gold_d]} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    event_command = input()

if town_info:
    print(f"Ahoy, Captain! There are {len(town_info)} wealthy settlements to go to:")
    for town in town_info:
        print(f"{town} -> Population: {town_info[town][population_d]} citizens, Gold: {town_info[town][gold_d]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
