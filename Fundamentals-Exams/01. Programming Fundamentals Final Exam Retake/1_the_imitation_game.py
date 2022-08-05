encrypted_message = [input()]


def move_msg(info):
    number_of_letters = int(info[0])
    encrypted_message[0] = f"{encrypted_message[0][number_of_letters:]}{encrypted_message[0][:number_of_letters]}"


def insert_msg(info):
    index_msg, value = info
    encrypted_message[0] = f"{encrypted_message[0][:index_msg]}{value}{encrypted_message[0][index_msg:]}"


def change_all(info):
    substring, replacement = info
    encrypted_message[0] = encrypted_message[0].replace(substring, replacement)


command_func = {
    "Move": move_msg,
    "Insert": insert_msg,
    "ChangeAll": change_all
}

command = input()
while command != "Decode":
    command_type, *info = (int(x) if x.isdigit() else x for x in command.split("|"))
    command_func[command_type](info)
    command = input()

print(f"The decrypted message is: {encrypted_message[0]}")








#
# main_string = input()
# command = input()
#
#
# def change_all(letter_one, letter_two, main_string):
#     return main_string.replace(letter_one, letter_two)
#
#
# def insert_test(number, symbol, main_string):
#     return main_string[:number] + symbol + main_string[number:]
#
#
# def move_string(number, main_string):
#     return main_string[number:] + main_string[:number]
#
#
# while command != "Decode":
#     command, *info = command.split("|")
#     if command == "Move":
#         number = int(info[0])
#         main_string = move_string(number, main_string)
#     else:
#         letter_one_or_number, letter_two_or_symbol = info
#         if command == "ChangeAll":
#             main_string = change_all(letter_one_or_number, letter_two_or_symbol, main_string)
#         elif command == "Insert":
#             main_string = insert_test(int(letter_one_or_number), letter_two_or_symbol, main_string)
#
#     command = input()
#
# print(f"The decrypted message is: {main_string}")
#







#
# main_string = input()
# command = input()
#
#
# def change_all(letter_one, letter_two):
#     global main_string
#     main_string = main_string.replace(letter_one, letter_two)
#
#
# def insert_test(number, symbol):
#     global main_string
#     main_string = main_string[:number] + symbol + main_string[number:]
#
#
# def move_string(number):
#     global main_string
#     main_string = main_string[number:] + main_string[:number]
#
#
# while command != "Decode":
#     command = command.split("|")
#     decode_command = command[0]
#     if decode_command == "ChangeAll":
#         letter_one = command[1]
#         letter_two = command[-1]
#         change_all(letter_one, letter_two)
#     elif decode_command == "Insert":
#         number = int(command[1])
#         symbol = command[-1]
#         insert_test(number, symbol)
#     elif decode_command == "Move":
#         number = int(command[1])
#         move_string(number)
#
#     command = input()
#
# print(f"The decrypted message is: {main_string}")
