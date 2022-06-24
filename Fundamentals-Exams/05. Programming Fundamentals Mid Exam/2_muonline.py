dungeons_rooms = input().split("|")

hero_info = {
    "bitcoins": 0,
    "health": 100,
}


def potions(points_command):
    if hero_info["health"] + points_command > 100:
        print(f"You healed for {100 - hero_info['health']} hp.")
        hero_info["health"] = 100
    else:
        hero_info["health"] += points_command
        print(f"You healed for {points_command} hp.")
    print(f"Current health: {hero_info['health']} hp.")


def chest(points_command):
    hero_info["bitcoins"] += points_command
    print(f"You found {points_command} bitcoins.")


for room, command in enumerate(dungeons_rooms, 1):
    type_command, points_command = [int(x) if x.isdigit() else x for x in command.split()]
    if type_command == "potion":
        potions(points_command)
    elif type_command == "chest":
        chest(points_command)
    else:
        hero_info['health'] -= points_command
    if all([hero_info['health'] > 0, type_command != "potion", type_command != "chest"]):
        print(f"You slayed {type_command}.")
    if hero_info['health'] <= 0:
        print(f"You died! Killed by {type_command}.")
        print(f"Best room: {room}")
        break
else:
    print("You've made it!")
    print(f"Bitcoins: {hero_info['bitcoins']}")
    print(f"Health: {hero_info['health']}")

#
#
# dungeons_rooms = input().split("|")
#
# hero_info = {
#     "bitcoins": 0,
#     "health": 100,
# }
# bitcoins = "bitcoins"
# health = "health"
# finish_dungeon = True
# for room, command in enumerate(dungeons_rooms):
#     command = command.split()
#     type_command = command[0]
#     points_command = int(command[-1])
#     if type_command == "potion":
#         if hero_info[health] + points_command > 100:
#             print(f"You healed for {100 - hero_info[health]} hp.")
#             hero_info[health] = 100
#         else:
#             hero_info[health] += points_command
#             print(f"You healed for {points_command} hp.")
#         print(f"Current health: {hero_info[health]} hp.")
#     elif type_command == "chest":
#         hero_info[bitcoins] += points_command
#         print(f"You found {points_command} bitcoins.")
#     else:
#         hero_info[health] -= points_command
#     if hero_info[health] > 0 and type_command != "potion" and type_command != "chest":
#         print(f"You slayed {type_command}.")
#     if hero_info[health] <= 0:
#         print(f"You died! Killed by {type_command}.")
#         print(f"Best room: {room + 1}")
#         finish_dungeon = False
#         break
#
# if finish_dungeon:
#     print("You've made it!")
#     print(f"Bitcoins: {hero_info[bitcoins]}")
#     print(f"Health: {hero_info[health]}")
