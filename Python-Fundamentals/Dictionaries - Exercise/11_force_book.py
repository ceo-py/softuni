force_command = input()

force_book = {}


def force_side(side_, user_):
    find_user = False
    for key in force_book:
        if user_ in force_book[key]:
            find_user = True
            break
    if side_ not in force_book:
        force_book[side_] = {}
    if not find_user:
        force_book[side_][user_] = user_


def force_change(user_, side_):
    for key in force_book:
        if user_ in force_book[key]:
            del force_book[key][user_]
            break
    if side_ not in force_book:
        force_book[side_] = {}
    force_book[side_][user_] = user_
    print(f"{user_} joins the {side_} side!")


while force_command != "Lumpawaroo":

    if " | " in force_command:
        force_command = force_command.split(" | ")
        force_side(str(force_command[0]), str(force_command[-1]))
    elif " -> " in force_command:
        force_command = force_command.split(" -> ")
        force_change(str(force_command[0]), str(force_command[-1]))
    force_command = input()

for side in force_book:
    if len(force_book[side]) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in force_book[side]:
            print(f"! {name}")