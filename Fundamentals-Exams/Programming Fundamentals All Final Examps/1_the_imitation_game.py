main_string = input()

command = input()


def move_sting(number, string):
    return string[number:] + string[:number]


def insert_string(index, value, string):
    return string[:index] + value + string[index:]


def change_all(substring, replacement, string):
    return string.replace(substring, replacement)


while command != "Decode":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split("|")]
    if command_type == "Move":
        number = info[0]
        main_string = move_sting(number, main_string)
    else:
        index_or_substring, value_or_replacement = info
        if command_type == "Insert":
            main_string = insert_string(index_or_substring, value_or_replacement, main_string)
        elif command_type == "ChangeAll":
            main_string = change_all(index_or_substring, value_or_replacement, main_string)

    command = input()

print(f"The decrypted message is: {main_string}")
