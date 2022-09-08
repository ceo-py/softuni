forces = {}


def add_user_to_side(name, side):
    for users in forces.values():
        if name in users:
            return
    forces[side] = forces.get(side, []) + [name]


def switch_side(side, name):
    for sides_, users in forces.items():
        if name in users:
            forces[sides_].remove(name)
            break
    forces[side] = forces.get(side, []) + [name]
    print(f"{name} joins the {side} side!")


command = input()

while command != "Lumpawaroo":
    if "|" in command:
        side, name = command.split(" | ")
        add_user_to_side(name, side)
    elif "->" in command:
        side, name = command.split(" -> ")
        switch_side(name, side)

    command = input()

for side, members in forces.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for user in members:
            print(f"! {user}")





#
#
# force_command = input()
#
# force_book = {}
#
#
# def force_side(side_, user_):
#     for key in force_book:
#         if user_ in force_book[key]:
#             return
#     force_book[side_] = force_book.get(side_, {})
#     force_book[side_][user_] = force_book.get(user_, side_)
#
#
# def force_change(user_, side_):
#     for key in force_book:
#         if user_ in force_book[key]:
#             del force_book[key][user_]
#             break
#     force_book[side_] = force_book.get(side_, {})
#     force_book[side_][user_] = force_book.get(user_, side_)
#     print(f"{user_} joins the {side_} side!")
#
#
# while force_command != "Lumpawaroo":
#
#     if " | " in force_command:
#         force_command = force_command.split(" | ")
#         force_side(str(force_command[0]), str(force_command[-1]))
#     elif " -> " in force_command:
#         force_command = force_command.split(" -> ")
#         force_change(str(force_command[0]), str(force_command[-1]))
#     force_command = input()
#
# for side in force_book:
#     if force_book[side]:
#         print(f"Side: {side}, Members: {len(force_book[side])}")
#         for name in force_book[side]:
#             print(f"! {name}")
