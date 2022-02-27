main_string = input()
command = input()


def change_all(letter_one, letter_two):
    global main_string
    main_string = main_string.replace(letter_one, letter_two)


def insert_test(number, symbol):
    global main_string
    main_string = main_string[:number] + symbol + main_string[number:]


def move_string(number):
    global main_string
    main_string = main_string[number:] + main_string[:number]


while command != "Decode":
    command = command.split("|")
    decode_command = command[0]
    if decode_command == "ChangeAll":
        letter_one = command[1]
        letter_two = command[-1]
        change_all(letter_one, letter_two)
    elif decode_command == "Insert":
        number = int(command[1])
        symbol = command[-1]
        insert_test(number, symbol)
    elif decode_command == "Move":
        number = int(command[1])
        move_string(number)

    command = input()

print(f"The decrypted message is: {main_string}")
