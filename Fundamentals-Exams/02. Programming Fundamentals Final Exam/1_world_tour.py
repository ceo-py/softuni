raw_string_stops = input()

command = input()


def valid_index(index):
    if 0 <= index < len(raw_string_stops):
        return True


def add_stop(index, string, main_string):
    if valid_index(index):
        main_string = main_string[:index] + string + main_string[index:]
    return main_string


def remove_stop(start_index, end_index, main_string):
    if valid_index(start_index) and valid_index(end_index):
        main_string = main_string[:start_index] + "" + main_string[end_index + 1:]
    return main_string


def switch(old_string, new_string, main_string):
    if old_string in main_string:
        main_string = main_string.replace(old_string, new_string)
    return main_string


while command != "Travel":
    command_type, index_or_old_string, end_index_or_string = [int(x) if x.isdigit() else x for x in command.split(":")]
    if "Add" in command_type:
        raw_string_stops = add_stop(index_or_old_string, end_index_or_string, raw_string_stops)
    elif "Remove" in command_type:
        raw_string_stops = remove_stop(index_or_old_string, end_index_or_string, raw_string_stops)
    elif "Switch" in command_type:
        raw_string_stops = switch(index_or_old_string, end_index_or_string, raw_string_stops)
    print(raw_string_stops)
    command = input()


print(f"Ready for world tour! Planned stops: {raw_string_stops}")






#
#
# main_destination = input()
# command = input()
#
#
# def add_stop(command_number, command_location):
#     global main_destination
#     how_long = int(len(main_destination))
#     if how_long - 1 >= command_number:
#         main_destination = main_destination[:command_number] + command_location + main_destination[command_number:]
#     print(main_destination)
#
#
# def remove_stop(command_number, command_location):
#     global main_destination
#     how_long = int(len(main_destination))
#     if how_long - 1 >= command_number and how_long - 1 >= command_location:
#         main_destination = main_destination[:command_number] + main_destination[1 + command_location:]
#     print(main_destination)
#
#
# def switch_stop(command_number, command_location):
#     global main_destination
#     if command_number in main_destination:
#         main_destination = main_destination.replace(command_number, command_location)
#     print(main_destination)
#
#
# while command != "Travel":
#     command = command.split(":")
#     command_type = command[0]
#     command_number = command[1]
#     command_location = command[2]
#     if command_type == "Add Stop":
#         add_stop(int(command_number), command_location)
#     elif command_type == "Remove Stop":
#         remove_stop(int(command_number), int(command_location))
#     elif command_type == "Switch":
#         switch_stop(command_number, command_location)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {main_destination}")
