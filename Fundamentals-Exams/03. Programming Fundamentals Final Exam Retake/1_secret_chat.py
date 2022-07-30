main_msg = input()
command = input()


def change_msg(substring, replacement, main_msg):
    return main_msg.replace(substring, replacement)


def inset_space(index, main_msg):
    return main_msg[:index] + " " + main_msg[index:]


def reverse(substring, main_msg):
    word_find = main_msg.find(substring)
    return main_msg[:word_find] + main_msg[word_find + (len(substring)):] + substring[::-1]


while command != "Reveal":
    command_type, *info = command.split(":|:")
    found_error = False
    if command_type == "ChangeAll":
        substring, replacement = info
        main_msg = change_msg(substring, replacement, main_msg)

    elif command_type == "Reverse":
        substring = info[0]
        if substring not in main_msg:
            print("error")
            found_error = True
        else:
            main_msg = reverse(substring, main_msg)

    elif command_type == "InsertSpace":
        index_for_insert = int(info[0])
        main_msg = inset_space(index_for_insert, main_msg)
    if not found_error:
        print(main_msg)

    command = input()

print(f"You have a new text message: {main_msg}")









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
