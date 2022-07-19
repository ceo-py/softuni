city = input()

city_info = {}

while city != "Sail":
    city_name, city_population, city_gold = [int(x) if x.isdigit() else x for x in city.split("||")]
    city_info[city_name] = city_info.get(city_name, {})
    city_info[city_name]["population"] = city_info[city_name].get("population", 0)
    city_info[city_name]["gold"] = city_info[city_name].get("gold", 0)
    city_info[city_name]["population"] += city_population
    city_info[city_name]["gold"] += city_gold
    city = input()


def plunder_town(town, people, gold, city_info):
    city_info[town]["population"] -= people
    city_info[town]["gold"] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if city_info[town]["population"] <= 0 or city_info[town]["gold"] <= 0:
        del city_info[town]
        print(f"{town} has been wiped off the map!")
    return city_info


def prosper_town(town, gold, city_info):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        city_info[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {city_info[town]['gold']} gold.")
    return city_info


events = input()

while events != "End":
    command, town, *other = [int(x) if x.isdigit() else x for x in events.split("=>")]
    if "Plunder" == command:
        city_info = plunder_town(town, int(other[0]), int(other[1]), city_info)
    elif "Prosper" == command:
        city_info = prosper_town(town, int(other[0]), city_info)
    events = input()

if city_info:
    print(f"Ahoy, Captain! There are {len(city_info.keys())} wealthy settlements to go to:")
    for town in city_info:
        print(f"{town} -> Population: {city_info[town]['population']} citizens, Gold: {city_info[town]['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")











#
# command = input()
#
# population_d = "population"
# cities_d = "cities"
# gold_d = "gold"
#
# town_info = {}
#
# while command != "Sail":
#     command = command.split("||")
#     name_town = command[0]
#     people_town = int(command[1])
#     gold_town = int(command[-1])
#     if name_town not in town_info:
#         town_info[name_town] = {}
#         town_info[name_town][population_d] = 0
#         town_info[name_town][gold_d] = 0
#     town_info[name_town][population_d] += people_town
#     town_info[name_town][gold_d] += gold_town
#     command = input()
#
# event_command = input()
#
# while event_command != "End":
#     event_command = event_command.split("=>")
#     type_command = event_command[0]
#     name_town = event_command[1]
#     people_town = int(event_command[2])
#     if type_command == "Plunder":
#         gold_town = int(event_command[-1])
#         town_info[name_town][gold_d] -= gold_town
#         town_info[name_town][population_d] -= people_town
#         print(f"{name_town} plundered! {gold_town} gold stolen, {people_town} citizens killed.")
#         if any([town_info[name_town][gold_d] <= 0, town_info[name_town][population_d] <= 0]):
#             print(f"{name_town} has been wiped off the map!")
#             del town_info[name_town]
#     elif type_command == "Prosper":
#         if people_town >= 0:
#             town_info[name_town][gold_d] += people_town
#             print(
#                 f"{people_town} gold added to the city treasury. {name_town} now has {town_info[name_town][gold_d]} gold.")
#         else:
#             print(f"Gold added cannot be a negative number!")
#     event_command = input()
#
# if town_info:
#     print(f"Ahoy, Captain! There are {len(town_info)} wealthy settlements to go to:")
#     for town in town_info:
#         print(f"{town} -> Population: {town_info[town][population_d]} citizens, Gold: {town_info[town][gold_d]} kg")
# else:
#     print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
