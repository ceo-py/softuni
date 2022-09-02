import os


def check_if_file_exist(name):
    try:
        with open(f"{name}", "r", encoding="utf-8") as file:
            return True, file.read()
    except FileNotFoundError:
        print("An error occurred")
        return False, 1


def create_file(info):
    file_name = info[0]
    with open(f"{file_name}", "w+", encoding="utf-8") as file:
        return


def save_file(name, data, mode, save_data=False):
    with open(f"{name}", f"{mode}", encoding="utf-8") as file:
        if save_data:
            file.write(data)
            if mode == "a":
                file.write("\n")


def add_text_to_file(info):
    file_name, text = info
    save_file(file_name, text, "a", True)


def replace_text_in_file(info):
    file_name, old_string, new_string = info
    file_exists, data = check_if_file_exist(file_name)
    if file_exists:
        data = data.replace(old_string, new_string)
        save_file(file_name, data, "w+", True)


def delete_file(info):
    file_name = info[0]
    file_exists, _ = check_if_file_exist(file_name)
    if file_exists:
        os.remove(file_name)


commands = {
    "Create": create_file,
    "Add": add_text_to_file,
    "Replace": replace_text_in_file,
    "Delete": delete_file
}
command = input()

while command != "End":
    command_type, *data = command.split("-")
    commands[command_type](data)
    command = input()
