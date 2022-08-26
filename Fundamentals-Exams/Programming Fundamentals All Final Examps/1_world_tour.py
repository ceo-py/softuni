main_string = input()


def valid_index(index):
    if 0 <= index < len(main_string):
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


command = input()

while command != "Travel":
    command_type, index_or_old_string, string_or_end_index = [int(x) if x.isdigit() else x for x in command.split(":")]
    if "Add" in command_type:
        main_string = add_stop(index_or_old_string, string_or_end_index, main_string)
    elif "Remove" in command_type:
        main_string = remove_stop(index_or_old_string, string_or_end_index, main_string)
    elif "Switch" in command_type:
        main_string = switch(index_or_old_string, string_or_end_index, main_string)
    print(main_string)
    command = input()


print(f"Ready for world tour! Planned stops: {main_string}")