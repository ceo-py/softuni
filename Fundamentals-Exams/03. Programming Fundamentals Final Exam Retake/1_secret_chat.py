raw_string_msg = [input()]


def insert_space(info):
    index_ = info[0]
    raw_string_msg[0] = f"{raw_string_msg[0][:index_]} {raw_string_msg[0][index_:]}"


def reverse_string(info):
    substring = info[0]
    if substring in raw_string_msg[0]:
        raw_string_msg[0] = raw_string_msg[0].replace(substring, "", 1) + substring[::-1]
    else:
        return "error"


def change_all(info):
    substring, replacement = info
    raw_string_msg[0] = raw_string_msg[0].replace(substring, replacement)


command_func = {
    "InsertSpace": insert_space,
    "Reverse": reverse_string,
    "ChangeAll": change_all
}

command = input()

while command != "Reveal":
    command_type, *info = (int(x) if x.isdigit() else x for x in command.split(":|:"))
    show = command_func[command_type](info)
    if "error" == show:
        print("error")
    else:
        print(raw_string_msg[0])
    command = input()

print(f"You have a new text message: {raw_string_msg[0]}")








#
# main_msg = input()
# command = input()
#
#
# while command != "Reveal":
#     command_type, *info = command.split(":|:")
#     found_error = False
#     if command_type == "ChangeAll":
#         main_msg = main_msg.replace(info[0], info[1])
#
#     elif command_type == "Reverse":
#         substring = info[0]
#         if substring not in main_msg:
#             print("error")
#             found_error = True
#         else:
#             main_msg = main_msg.replace(substring, "", 1) + substring[::-1]
#
#     elif command_type == "InsertSpace":
#         index_for_insert = int(info[0])
#         main_msg = main_msg[:index_for_insert] + " " + main_msg[index_for_insert:]
#
#     if not found_error:
#         print(main_msg)
#
#     command = input()
#
# print(f"You have a new text message: {main_msg}")








#
#
#
# main_msg = input()
# command = input()
#
#
# def change_msg(substring, replacement):
#     global main_msg
#     main_msg = main_msg.replace(substring, replacement)
#     print(main_msg)
#
#
# def inset_space(index):
#     global main_msg
#     main_msg = main_msg[:index] + " " + main_msg[index:]
#     print(main_msg)
#
#
# def reverse(substring):
#     global main_msg
#     if substring in main_msg:
#         word_find = main_msg.find(substring)
#         main_msg = main_msg[:word_find] + "" + main_msg[word_find + (len(substring)):]
#         main_msg += substring[::-1]
#         print(main_msg)
#     else:
#         print("error")
#
#
# while command != "Reveal":
#     command = command.split(":|:")
#     command_type = command[0]
#     if command_type == "ChangeAll":
#         substring = command[1]
#         replacement = command[-1]
#         change_msg(substring, replacement)
#
#     elif command_type == "Reverse":
#         substring = command[1]
#         reverse(substring)
#
#     elif command_type == "InsertSpace":
#         index_for_insert = int(command[-1])
#         inset_space(index_for_insert)
#
#     command = input()
#
# print(f"You have a new text message: {main_msg}")
