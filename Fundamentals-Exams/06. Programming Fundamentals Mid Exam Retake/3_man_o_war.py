pirate_ship = [int(x) for x in input().split('>')]
warship_ship = [int(x) for x in input().split('>')]
max_health_capacity = int(input())

command_data = input()

while command_data != 'Retire':
    command, *data = [int(x) if x[-1].isdigit() else x for x in command_data.split()]

    if command == 'Fire':
        index, damage = data
        # if index in range(len(warship_ship)):
        if 0 <= index < len(warship_ship):
            warship_ship[index] -= damage
            if warship_ship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                break

    elif command == 'Defend':
        start_index, end_index, damage = data
        # if 0 <= start_index < end_index <= len(pirate_ship):

        if all(x in range(len(pirate_ship)) for x in [start_index, end_index]):
            game_over = False
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    game_over = True
                    break
            if game_over:
                break

    elif command == 'Repair':
        index, health = data
        # if index in range(len(pirate_ship)):
        if 0 <= index < len(pirate_ship):
            # pirate_ship[index] = max_health_capacity if pirate_ship[index] \
            #                                             + health > max_health_capacity \
            #     else max_health_capacity + health

            if pirate_ship[index] + health > max_health_capacity:
                health = max_health_capacity - pirate_ship[index]

            pirate_ship[index] += health

    elif command == 'Status':
        lower_capacity = max_health_capacity * 0.20
        count = sum(1 for x in pirate_ship if x < lower_capacity)
        print(f'{count} sections need repair.')

    command_data = input()

else:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship_ship)}')











# pirate_ship = [int(x) for x in input().split(">")]
# war_ship = [int(x) for x in input().split(">")]
# maximum_health = int(input())
# data_info = input()
#
# while data_info != "Retire":
#     if data_info == "Status":
#         count = sum(1 for x in pirate_ship if (x / maximum_health) * 100 < 20)
#         print(f"{count} sections need repair.")
#         data_info = input()
#         continue
#
#     command, *data = [int(x) if x[-1].isdigit() else x for x in data_info.split()]
#
#     if command == "Fire":
#         index, damage = data
#         if 0 <= index < len(war_ship):
#             war_ship[index] -= damage
#             if war_ship[index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 exit()
#
#     elif command == "Defend":
#         start_index, end_index, damage = data
#         if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#             for x in range(start_index, end_index + 1):
#                 pirate_ship[x] -= damage
#                 if pirate_ship[x] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     exit()
#
#     elif command == "Repair":
#         index, health = data
#         if 0 <= index < len(pirate_ship):
#             if pirate_ship[index] + health > maximum_health:
#                 health = maximum_health - pirate_ship[index]
#             pirate_ship[index] += health
#
#     data_info = input()
#
# print(f"Pirate ship status: {sum(pirate_ship)}")
# print(f"Warship status: {sum(war_ship)}")
#







#
#
# pirate_ship, warship, maximum_health = [int(n) for n in input().split(">")], [int(n) for n in input().split(">")], int(
#     input())
# command = input()
#
#
# def status_ship():
#     repair_counter = 0
#     for hp in pirate_ship:
#         if ((hp / maximum_health) * 100) < 20.00:
#             repair_counter += 1
#     if repair_counter:
#         print(f"{repair_counter} sections need repair.")
#
#
# def fire_ship(index, damage):
#     if 0 <= index < len(warship):
#         warship[index] -= damage
#         if warship[index] <= 0:
#             print(f"You won! The enemy ship has sunken.")
#             exit()
#
#
# def defend_ship(start_index, end_index, damage):
#     if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#         for index in range(start_index, end_index + 1):
#             pirate_ship[index] -= damage
#             if pirate_ship[index] <= 0:
#                 print(f"You lost! The pirate ship has sunken.")
#                 exit()
#
#
# def repair_ship(index, health):
#     if 0 <= index < len(pirate_ship):
#         pirate_ship[index] += health
#         if pirate_ship[index] > maximum_health:
#             pirate_ship[index] = maximum_health
#
#
# while command != "Retire":
#     command = command.split()
#     type_command = command[0]
#     if type_command == "Status":
#         status_ship()
#     else:
#         index_ship, damage_or_health_ship = int(command[1]), int(command[2])
#     if type_command == "Fire":
#         fire_ship(index_ship, damage_or_health_ship)
#     elif type_command == "Defend":
#         defend_ship(index_ship, damage_or_health_ship, int(command[-1]))
#     elif type_command == "Repair":
#         repair_ship(index_ship, damage_or_health_ship)
#     command = input()
#
# if len(pirate_ship) and len(warship) > 0:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(warship)}")
