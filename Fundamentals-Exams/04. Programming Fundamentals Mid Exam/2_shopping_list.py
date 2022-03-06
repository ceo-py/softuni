groceries = input().split("!")


def urgent_item(item):
    if item not in groceries:
        groceries.insert(0, item)


def unnecessary_item(item):
    if item in groceries:
        groceries.remove(item)


def correct_item(old_item, new_item):
    if old_item in groceries:
        groceries[groceries.index(old_item)] = new_item


def rearrange_item(item):
    if item in groceries:
        groceries.remove(item)
        groceries.append(item)


command = input()
while command != "Go Shopping!":
    command = command.split()
    type_command = command[0]
    item_command = command[1]
    if type_command == "Urgent":
        urgent_item(item_command)
    elif type_command == "Unnecessary":
        unnecessary_item(item_command)
    elif type_command == "Correct":
        correct_item(item_command, command[-1])
    elif type_command == "Rearrange":
        rearrange_item(item_command)

    command = input()

print(*groceries, sep=", ")
