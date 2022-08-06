raw_string_stops = [input()]
command = input()


def valid_index(index):
    if 0 <= index < len(raw_string_stops[0]):
        return True


def add_stop(index, string):
    if valid_index(index):
        raw_string_stops[0] = f"{raw_string_stops[0][:index]}{string}{raw_string_stops[0][index:]}"


def remove_stop(start_index, end_index):
    if valid_index(start_index) and valid_index(end_index):
        raw_string_stops[0] = f"{raw_string_stops[0][:start_index]}{raw_string_stops[0][end_index + 1:]}"


def switch(old_string, new_string):
    if old_string in raw_string_stops[0]:
        raw_string_stops[0] = raw_string_stops[0].replace(old_string, new_string)


commands_func = {
    "Add Stop": add_stop,
    "Remove Stop": remove_stop,
    "Switch": switch
}

while command != "Travel":
    command_type, index_or_old_string, end_index_or_string = [int(x) if x.isdigit() else x for x in command.split(":")]
    commands_func[command_type](index_or_old_string, end_index_or_string)
    print(raw_string_stops[0])
    command = input()

print(f"Ready for world tour! Planned stops: {raw_string_stops[0]}")










#
# raw_string_stops = input()
#
# command = input()
#
#
# def valid_index(index):
#     if 0 <= index < len(raw_string_stops):
#         return True
#
#
# def add_stop(index, string, main_string):
#     if valid_index(index):
#         main_string = main_string[:index] + string + main_string[index:]
#     return main_string
#
#
# def remove_stop(start_index, end_index, main_string):
#     if valid_index(start_index) and valid_index(end_index):
#         main_string = main_string[:start_index] + "" + main_string[end_index + 1:]
#     return main_string
#
#
# def switch(old_string, new_string, main_string):
#     if old_string in main_string:
#         main_string = main_string.replace(old_string, new_string)
#     return main_string
#
#
# commands_func = {
#     "Add Stop": add_stop,
#     "Remove Stop": remove_stop,
#     "Switch": switch
# }
#
# while command != "Travel":
#     command_type, index_or_old_string, end_index_or_string = [int(x) if x.isdigit() else x for x in command.split(":")]
#     raw_string_stops = commands_func[command_type](index_or_old_string, end_index_or_string, raw_string_stops)
#     print(raw_string_stops)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {raw_string_stops}")






#
# encrypted_message = [input()]
#
#
# def check_valid_index(index_):
#     if 0 <= index_ < len(encrypted_message[0]):
#         return True
#
#
# def add_stop(info):
#     index_, string_ = info
#     if check_valid_index(index_):
#         encrypted_message[0] = f"{encrypted_message[0][:index_]}{string_}{encrypted_message[0][index_:]}"
#         return True
#
#
# def remove_stop(info):
#     start_index, end_index = info
#     if check_valid_index(start_index) and check_valid_index(end_index):
#         encrypted_message[0] = f"{encrypted_message[0][:start_index]}{encrypted_message[0][start_index + end_index:]}"
#         return True
#
#
# def switch_msg(info):
#     old_string, new_string = info
#     if old_string in encrypted_message[0]:
#         encrypted_message[0] = encrypted_message[0].replace(old_string, new_string)
#         return True
#
#
# command_func = {
#     "Add Stop": add_stop,
#     "Remove Stop": remove_stop,
#     "Switch": switch_msg
# }
#
# command = input()
#
# while command != "Travel":
#     command_type, *info = (int(x) if x.isdigit() else x for x in command.split(":"))
#     if command_func[command_type](info):
#         print(encrypted_message[0])
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {encrypted_message[0]}")
#
#
#
#






#
# class TourStops:
#     def __init__(self, stops):
#         self.stops = stops
#
#     def check_valid_index(self, index):
#         if 0 <= index < len(self.stops):
#             return True
#
#     def add_stop(self, start_index: int, string_to_add: str):
#         if self.check_valid_index(start_index):
#             self.stops = f"{self.stops[:start_index]}{string_to_add}{self.stops[start_index:]}"
#
#     def remove_stop(self, start_index: int, end_index: int):
#         if self.check_valid_index(start_index) and self.check_valid_index(end_index):
#             self.stops = f"{self.stops[:start_index]}{self.stops[end_index + 1:]}"
#
#     def switch_(self, old_string: str, new_string):
#         if old_string in self.stops:
#             self.stops = self.stops.replace(old_string, new_string)
#
#     def __str__(self):
#         return self.stops
#
#
# stops_info = TourStops(input())
#
# command = input()
#
# while command != "Travel":
#     command_type, *info = [int(x) if x.isdigit() else x for x in command.split(":")]
#     if command_type == "Add Stop":
#         stops_info.add_stop(int(info[0]), info[1])
#     elif command_type == "Remove Stop":
#         stops_info.remove_stop(int(info[0]), int(info[1]))
#     elif command_type == "Switch":
#         stops_info.switch_(info[0], info[1])
#     print(stops_info)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {stops_info}")
#
#
#




#
#
# raw_string_stops = input()
#
# command = input()
#
#
# def valid_index(index):
#     if 0 <= index < len(raw_string_stops):
#         return True
#
#
# def add_stop(index, string, main_string):
#     if valid_index(index):
#         main_string = main_string[:index] + string + main_string[index:]
#     return main_string
#
#
# def remove_stop(start_index, end_index, main_string):
#     if valid_index(start_index) and valid_index(end_index):
#         main_string = main_string[:start_index] + "" + main_string[end_index + 1:]
#     return main_string
#
#
# def switch(old_string, new_string, main_string):
#     if old_string in main_string:
#         main_string = main_string.replace(old_string, new_string)
#     return main_string
#
#
# while command != "Travel":
#     command_type, index_or_old_string, end_index_or_string = [int(x) if x.isdigit() else x for x in command.split(":")]
#     if "Add" in command_type:
#         raw_string_stops = add_stop(index_or_old_string, end_index_or_string, raw_string_stops)
#     elif "Remove" in command_type:
#         raw_string_stops = remove_stop(index_or_old_string, end_index_or_string, raw_string_stops)
#     elif "Switch" in command_type:
#         raw_string_stops = switch(index_or_old_string, end_index_or_string, raw_string_stops)
#     print(raw_string_stops)
#     command = input()
#
#
# print(f"Ready for world tour! Planned stops: {raw_string_stops}")
#
#




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
