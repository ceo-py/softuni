dungeon_rooms = input().split("|")

hero_health = 100
hero_collected_bitcoins = 0

for i in range(len(dungeon_rooms)):

    command, number = [int(x) if x[-1].isdigit() else x for x in dungeon_rooms[i].split()]

    if command == 'potion':

        if hero_health + number > 100:
            number = 100 - hero_health

        hero_health += number

        print(f'You healed for {number} hp.')
        print(f'Current health: {hero_health} hp.')
        continue

    if command == 'chest':
        hero_collected_bitcoins += number
        print(f'You found {number} bitcoins.')
        continue


    hero_health -= number

    if hero_health > 0:
        print(f'You slayed {command}.')
        continue

    print(f'You died! Killed by {command}.')
    print(f'Best room: {i + 1}')
    break

else:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {hero_collected_bitcoins}')
    print(f'Health: {hero_health}')





#
# dungeon_rooms = input().split("|")
#
# hero_health = 100
# hero_collected_bitcoins = 0
#
# for room_data in dungeon_rooms:
#
#     command, number = [int(x) if x[-1].isdigit() else x for x in room_data.split()]
#
#     if command == 'potion':
#
#         if hero_health + number >= 100:
#             number = 100 - hero_health
#
#         hero_health += number
#
#         print(f'You healed for {number} hp.')
#         print(f'Current health: {hero_health} hp.')
#         continue
#
#     if command == 'chest':
#         hero_collected_bitcoins += number
#         print(f'You found {number} bitcoins.')
#         continue
#
#
#     hero_health -= number
#
#     if hero_health > 0:
#         print(f'You slayed {command}.')
#         continue
#
#     print(f'You died! Killed by {command}.')
#     print(f'Best room: {dungeon_rooms.index(room_data) + 1}')
#     break
#
# else:
#     print(f'You\'ve made it!')
#     print(f'Bitcoins: {hero_collected_bitcoins}')
#     print(f'Health: {hero_health}')
#
#






# rooms_data = [data.split() for data in input().split("|")]
#
#
# initial_health = 100
# bitcoins = 0
# room = 0
#
# for room_data in rooms_data:
#     item, value = [int(x) if x.isdigit() else x for x in room_data]
#     room += 1
#
#     if item == "potion":
#         if initial_health + value > 100:
#             value = 100 - initial_health
#         initial_health += value
#         print(f"You healed for {value} hp.")
#         print(f"Current health: {initial_health} hp.")
#
#     elif item == "chest":
#         bitcoins += value
#         print(f"You found {value} bitcoins.")
#
#     else:
#         if initial_health - value <= 0:
#             print(f"You died! Killed by {item}.")
#             print(f"Best room: {room}")
#             break
#         else:
#             initial_health -= value
#             print(f"You slayed {item}.")
# else:
#     print("You've made it!")
#     print(f"Bitcoins: {bitcoins}")
#     print(f"Health: {initial_health}")







#
#
# dungeons_rooms = input().split("|")
#
# hero_info = {
#     "bitcoins": 0,
#     "health": 100,
# }
#
#
# def potions(points_command):
#     if hero_info["health"] + points_command > 100:
#         print(f"You healed for {100 - hero_info['health']} hp.")
#         hero_info["health"] = 100
#     else:
#         hero_info["health"] += points_command
#         print(f"You healed for {points_command} hp.")
#     print(f"Current health: {hero_info['health']} hp.")
#
#
# def chest(points_command):
#     hero_info["bitcoins"] += points_command
#     print(f"You found {points_command} bitcoins.")
#
#
# for room, command in enumerate(dungeons_rooms, 1):
#     type_command, points_command = [int(x) if x.isdigit() else x for x in command.split()]
#     if type_command == "potion":
#         potions(points_command)
#     elif type_command == "chest":
#         chest(points_command)
#     else:
#         hero_info['health'] -= points_command
#     if all([hero_info['health'] > 0, type_command != "potion", type_command != "chest"]):
#         print(f"You slayed {type_command}.")
#     if hero_info['health'] <= 0:
#         print(f"You died! Killed by {type_command}.")
#         print(f"Best room: {room}")
#         break
# else:
#     print("You've made it!")
#     print(f"Bitcoins: {hero_info['bitcoins']}")
#     print(f"Health: {hero_info['health']}")
#



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
