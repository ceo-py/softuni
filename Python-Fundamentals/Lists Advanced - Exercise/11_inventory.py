collecting_items = [n for n in input().split(", ")]


def Collect(item):
    if item not in collecting_items:
        collecting_items.append(item)


def Drop(item):
    if item in collecting_items:
        collecting_items.remove(item)


def Combine(item_one, item_two):
    if item_one in collecting_items:
        index_item_one = collecting_items.index(item_one)
        collecting_items.insert((index_item_one + 1), item_two)


def Renew(item):
    if item in collecting_items:
        collecting_items.append(collecting_items.pop(collecting_items.index(item)))


command_list = [Collect, Drop, Combine, Renew]
command = input()
while command != "Craft!":
    type_command, item = command.split(" - ")
    for function in command_list:
        if " " in type_command:
            type_command,_ = type_command.split()
        if function.__name__ == type_command:
            if ":" not in item:
                function(item)
            else:
                item_one, item_two = item.split(":")
                function(item_one, item_two)
            break
    command = input()

print(", ".join(collecting_items))



# collecting_items = [n for n in input().split(", ")]
#
#
# def collecting(item):
#     if item not in collecting_items:
#         collecting_items.append(item)
#
#
# def droping(item):
#     if item in collecting_items:
#         collecting_items.remove(item)
#
#
# def combine_items(item_one, item_two):
#     if item_one in collecting_items:
#         index_item_one = collecting_items.index(item_one)
#         collecting_items.insert((index_item_one + 1), item_two)
#
#
# def renew(item):
#     if item in collecting_items:
#         collecting_items.append(collecting_items.pop(collecting_items.index(item)))
#
#
# command = input()
# while command != "Craft!":
#     if "Combine Items" in command:
#         command = command.split("- ")[1].lstrip().split(":")
#         combine_items(command[0], command[-1])
#     else:
#         command = command.split(" - ")
#     if "Collect" in command:
#         collecting(command[-1])
#     elif "Drop" in command:
#         droping(command[-1])
#     elif "Renew" in command:
#         renew(command[-1])
#     command = input()
#
# print(*collecting_items, sep=", ")



# collecting_items = [n for n in input().split(", ")]
#
#
# def collecting(item):
#     if item not in collecting_items:
#         collecting_items.append(item)
#
#
# def droping(item):
#     if item in collecting_items:
#         collecting_items.remove(item)
#
#
# def combine_items(item_one, item_two):
#     if item_one in collecting_items:
#         index_item_one = collecting_items.index(item_one)
#         collecting_items.insert((index_item_one + 1), item_two)
#
#
# def renew(item):
#     if item in collecting_items:
#         index_item = collecting_items.index(item)
#         getting_the_item = collecting_items.pop(index_item)
#         collecting_items.append(getting_the_item)
#
#
# while True:
#
#     command = input()
#
#     if "Craft!" in command:
#         break
#
#     if "Combine Items" in command:
#         command = command.split("- ")[1].lstrip().split(":")
#         combine_items(command[0], command[-1])
#
#     else:
#         command = command.split(" - ")
#
#     if "Collect" in command:
#         collecting(command[-1])
#
#     elif "Drop" in command:
#         droping(command[-1])
#
#     elif "Renew" in command:
#         renew(command[-1])
#
# print(*collecting_items, sep=", ")
