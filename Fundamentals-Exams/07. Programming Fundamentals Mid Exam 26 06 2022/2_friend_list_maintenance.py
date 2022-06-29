user_names_to_store = input().split(", ")
command = input()


def valid_index(index):
    if 0 <= index < len(user_names_to_store):
        return True


def blacklist(name):
    if name in user_names_to_store:
        name_index = user_names_to_store.index(name)
        user_names_to_store[name_index] = "Blacklisted"
        print(f"{name} was blacklisted.")
    else:
        print(f"{name} was not found.")


def error(index):
    if valid_index(index) and ("Lost" != user_names_to_store[index] != "Blacklisted"):
        print(f"{user_names_to_store[index]} was lost due to an error.")
        user_names_to_store[index] = "Lost"


def change(index, new_name):
    if valid_index(index):
        print(f"{user_names_to_store[index]} changed his username to {new_name}")
        user_names_to_store[index] = new_name


def result_show():
    print(f"Blacklisted names: {len([x for x in user_names_to_store if x == 'Blacklisted'])}")
    print(f"Lost names: {len([x for x in user_names_to_store if x == 'Lost'])}")
    print(*user_names_to_store)


while command != "Report":
    if "Change" in command:
        _, index, name = [int(x) if x.isdigit() else x for x in command.split()]
        change(index, name)
    else:
        name_or_index = command.split()[-1]
        if "Blacklist" in command:
            blacklist(name_or_index)
        elif "Error" in command:
            error(int(name_or_index))

    command = input()

result_show()


