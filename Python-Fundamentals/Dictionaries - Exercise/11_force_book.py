command = input()
force_side = {}


def create_side(name, side):
    duplicate_name = False
    duplicate_force = False
    if side not in force_side:
        force_side[side] = {}
    else:
        for side_name in force_side:
            if side_name == side:
                duplicate_force = True
            for key, value in force_side[side_name].items():
                if value == name:
                    duplicate_name = True
                    break
            if duplicate_name:
                break
    if not duplicate_name:
        force_side[side][name] = name
    if not duplicate_force:
        force_side[side] = {}
        force_side[side][name] = name


def join_side(name, side):
    duplicate_name = False
    side_name_check = False
    for side_name in force_side:
        if side_name == side:
            side_name_check = True
        for key, value in force_side[side_name].items():
            if value == name:
                duplicate_name = True
                force_side[side_name].pop(key)
                break
        if duplicate_name:
            break

    if not duplicate_name:
        force_side[side][name] = name
    elif not side_name_check:
        force_side[side] = {}
        force_side[side][name] = name
    else:
        force_side[side][name] = name

    print(f"{name} joins the {side} side!")


def result_show():
    for side in force_side:
        members = len(force_side[side])
        if members != 0:
            print(f"Side: {side}, Members: {members}")
            for key, value in force_side[side].items():
                print(f"! {value}")


while command != "Lumpawaroo":
    is_it_side = command.count('|')
    if is_it_side != 0:
        command = command.split(" | ")
        side = command[0]
        name = command[-1]
        create_side(name, side)
    else:
        command = command.split(" -> ")
        name = command[0]
        side = command[-1]
        join_side(name, side)

    command = input()

result_show()
