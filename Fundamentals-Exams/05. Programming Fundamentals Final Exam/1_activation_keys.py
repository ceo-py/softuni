main_string = input()


def string_contains(substring, main_string):
    if substring in main_string:
        return f"{main_string} contains {substring}"
    return "Substring not found!"


def flip_string(type_letters, start_index, end_index, main_string):
    if "Upper" in type_letters:
        result = main_string[:start_index] + main_string[start_index:end_index].upper() \
                 + main_string[end_index:]
    elif "Lower" in type_letters:
        result = main_string[:start_index] + main_string[start_index:end_index].lower() \
                 + main_string[end_index:]
    return result


def slice_string(start_index, end_index, main_string):
    return main_string[:start_index] + main_string[end_index:]


command = input()

while command != "Generate":
    command_name, *others = command.split(">>>")
    if "Contains" == command_name:
        print(string_contains(others[0], main_string))
    elif "Flip" == command_name:
        type_letters, start_index, end_index = others
        main_string = flip_string(type_letters, int(start_index), int(end_index), main_string)
    elif "Slice" == command_name:
        start_index, end_index = others
        main_string = slice_string(int(start_index), int(end_index), main_string)
    if "Contains" != command_name:
        print(main_string)

    command = input()

print(f"Your activation key is: {main_string}")









#
#
# main_string = input()
#
# def string_contains(substring, main_string):
#     if substring in main_string:
#         print(f"{main_string} contains {substring}")
#     else:
#         print("Substring not found!")
#     return main_string
#
#
# def flip_string(type_letters, start_index, end_index, main_string):
#     if "Upper" in type_letters:
#         result = main_string[:start_index] + main_string[start_index:end_index].upper() \
#                  + main_string[end_index:]
#     elif "Lower" in type_letters:
#         result = main_string[:start_index] + main_string[start_index:end_index].lower() \
#                  + main_string[end_index:]
#     print(result)
#     return result
#
#
# def slice_string(start_index, end_index, main_string):
#     main_string = main_string[:start_index] + main_string[end_index:]
#     print(main_string)
#     return main_string
#
#
# command = input()
#
# while command != "Generate":
#     command_name, *others = command.split(">>>")
#     if "Contains" == command_name:
#         main_string = string_contains(others[0], main_string)
#     elif "Flip" == command_name:
#         main_string = flip_string(others[0], int(others[1]), int(others[2]), main_string)
#     elif "Slice" == command_name:
#         main_string = slice_string(int(others[0]), int(others[1]), main_string)
#
#     command = input()
#
# print(f"Your activation key is: {main_string}")
#
#





#
#
#
# main_string = input()
#
# command = input()
#
# while command != "Generate":
#     command = command.split(">>>")
#     type_command = command[0]
#     if type_command == "Contains":
#         letters = command[-1]
#         if letters in main_string:
#             print(f"{main_string} contains {letters}")
#         else:
#             print("Substring not found!")
#     elif type_command == "Flip":
#         low_or_up = command[1]
#         start_index = int(command[2])
#         end_index = int(command[3])
#         if low_or_up == "Upper":
#             result = (main_string[start_index:end_index]).upper()
#         else:
#             result = (main_string[start_index:end_index]).lower()
#         main_string = main_string[:start_index] + result + main_string[end_index:]
#         print(main_string)
#     elif type_command == "Slice":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         main_string = main_string[:start_index] + main_string[end_index:]
#         print(main_string)
#
#     command = input()
#
# print(f"Your activation key is: {main_string}")
