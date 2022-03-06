items_collect = input().split(", ")

command = input()

while command != "Craft!":
    command = command.split(" - ")
    type_command = command[0]
    item = command[1]
    if type_command == "Collect":
        if item not in items_collect:
            items_collect.append(item)
    elif type_command == "Drop":
        if item in items_collect:
            items_collect.remove(item)
    elif type_command == "Renew":
        if item in items_collect:
            items_collect.remove(item)
            items_collect.append(item)
    elif type_command == "Combine Items":
        item = command[1].split(":")
        if item[0] in items_collect:
            items_collect.insert(items_collect.index(item[0]) + 1, item[1])
    command = input()

print(*items_collect, sep=", ")
