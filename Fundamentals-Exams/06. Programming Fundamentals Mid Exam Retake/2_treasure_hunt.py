initial_loot = input().split('|')

command_data = input()

while command_data != 'Yohoho!':
    command, *data = [int(x) if x.isdigit() else x for x in command_data.split()]

    if command == 'Loot':
        # [initial_loot.append(item) for item in data if item not in initial_loot]
        for item in data:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command == 'Drop':
        index = data[0]
        if index in range(len(initial_loot)):
            # item = initial_loot.pop(initial_loot)
            # initial_loot.append(initial_loot)

            initial_loot.append(initial_loot.pop(index))

    elif command == 'Steal':
        index = -data[0]
        stolen_items = initial_loot[index:]
        initial_loot = initial_loot[:index]
        print(', '.join(stolen_items))

    command_data = input()


if initial_loot:
    # avr_treasure = 0
    # for item in initial_loot:
    #     avr_treasure += len(initial_loot)

    avr_treasure = sum(len(x) for x in initial_loot) / len(initial_loot)
    print(f'Average treasure gain: {avr_treasure:.2f} pirate credits.')

else:
    print('Failed treasure hunt.')




# initial_loot = input().split("|")
#
# data_info = input()
#
# while data_info != "Yohoho!":
#     command, *data = [x for x in data_info.split()]
#
#     if command == "Loot":
#         for item in data:
#             if item not in initial_loot:
#                 initial_loot.insert(0, item)
#
#     elif command == "Drop":
#         index = int(data[0])
#         if 0 <= index < len(initial_loot):
#             initial_loot.append(initial_loot.pop(index))
#
#     elif command == "Steal":
#         count = int(data[0])
#         stolen_items = initial_loot[-count:]
#         initial_loot = initial_loot[:-count]
#         print(*stolen_items, sep=", ")
#     data_info = input()
#
#
# if initial_loot:
#     average_treasure_gain = sum(len(x) for x in initial_loot) / len(initial_loot)
#     print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
# else:
#     print("Failed treasure hunt.")





#
#
# initial_loot = input().split("|")
#
# data_info = input()
#
#
# def loot(*data):
#     for item in data:
#         if item not in initial_loot:
#             initial_loot.insert(0, item)
#
#
# def drop(index):
#     if 0 <= index < len(initial_loot):
#         initial_loot.append(initial_loot.pop(index))
#
#
# def steal(count):
#     global initial_loot
#     stolen_items = initial_loot[-count:]
#     initial_loot = initial_loot[:-count]
#     print(*stolen_items, sep=", ")
#
#
# commands = {
#     "Loot": loot,
#     "Drop": drop,
#     "Steal": steal
# }
#
# while data_info != "Yohoho!":
#     command, *data = [x if x.isalpha() else int(x) for x in data_info.split()]
#     commands[command](*data)
#     data_info = input()
#
# if initial_loot:
#     average_treasure_gain = sum(len(x) for x in initial_loot) / len(initial_loot)
#     print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
# else:
#     print("Failed treasure hunt.")
#
#
#






#
#
#
# main_treasure_check = input().split("|")
#
# command = input()
#
#
# def loot_(command):
#     for index, item in enumerate(command):
#         if index != 0 and item not in main_treasure_check:
#             main_treasure_check.insert(0, item)
#
#
# def drop_(command):
#     index_item = int(command[-1])
#     if abs(index_item) < len(main_treasure_check):
#         main_treasure_check.append(main_treasure_check.pop(index_item))
#
#
# def steal_(command):
#     global main_treasure_check
#     count_items = int(command[-1])
#     stolen_items = main_treasure_check[-count_items:]
#     main_treasure_check = main_treasure_check[:-count_items]
#     print(*stolen_items, sep=", ")
#
#
# def show_result():
#     if main_treasure_check:
#         print(f"Average treasure gain: {(sum(len(item) for item in main_treasure_check) / len(main_treasure_check)):.2f} pirate credits.")
#     else:
#         print(f"Failed treasure hunt.")
#
#
# while command != "Yohoho!":
#     command = command.split()
#     if "Loot" in command:
#         loot_(command)
#     elif "Drop" in command:
#         drop_(command)
#     elif "Steal" in command:
#         steal_(command)
#     command = input()
#
# show_result()
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # main_treasure_check = input().split("|")
# #
# # command = input()
# #
# # while command != "Yohoho!":
# #     command = command.split()
# #     type_command = command[0]
# #     if type_command == "Loot":
# #         for index, item in enumerate(command):
# #             if index != 0 and item not in main_treasure_check:
# #                 main_treasure_check.insert(0, item)
# #     elif type_command == "Drop":
# #         index_item = int(command[-1])
# #         if abs(index_item) < len(main_treasure_check):
# #             main_treasure_check.append(main_treasure_check.pop(index_item))
# #     elif type_command == "Steal":
# #         count_items = int(command[-1])
# #         stolen_items = main_treasure_check[-count_items:]
# #         main_treasure_check = main_treasure_check[:-count_items]
# #         print(*stolen_items, sep=", ")
# #
# #     command = input()
# #
# # if main_treasure_check:
# #     average_treasure = 0
# #     for item in main_treasure_check:
# #         average_treasure += len(item)
# #     print(f"Average treasure gain: {(average_treasure / len(main_treasure_check)):.2f} pirate credits.")
# # else:
# #     print(f"Failed treasure hunt.")
