import os


def check_if_file_exist(name):
    try:
        with open(f"{name}", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("An error occurred")


def create_file(file_name):
    with open(f"{file_name}", "w+", encoding="utf-8") as file:
        return


def save_file(name, data, mode):
    with open(f"{name}", f"{mode}", encoding="utf-8") as file:
        file.write(data)
        if mode == "a":
            file.write("\n")


def add_text_to_file(file_name, text):
    save_file(file_name, text, "a")


def replace_text_in_file(file_name, old_string, new_string):
    data = check_if_file_exist(file_name)
    if data:
        data = data.replace(old_string, new_string)
        save_file(file_name, data, "w+")


def delete_file(file_name):
    file_exists = check_if_file_exist(file_name)
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
    commands[command_type](*data)
    command = input()
