command = input()

dwarf_info = {}
result = {}

def add_dwarf(name, color, physic):
    if color not in dwarf_info:
        dwarf_info[color] = {}
    if name not in dwarf_info[color]:
        dwarf_info[color][name] = physic
    if physic > dwarf_info[color][name]:
        dwarf_info[color][name] = physic


def show_result():
    for color in dwarf_info:
        total = dwarf_info[color].values()
        result[color] = sum(total)
    resultt = sorted(result.items(), key=lambda x: x[1], reverse=True)
    for color in resultt:
        result[color] = 0
        for key, value in dwarf_info[color[0]].items():
            result[color] += value
        # resultt = sorted(result[color].values(), key=lambda x: x[1], reverse=True)
    for color in resultt:
        for key, value in dwarf_info[color[0]].items():
            print(f"({color[0]}) {key} <-> {value}")


while command != "Once upon a time":
    command = command.split(" <:> ")
    name = command[0]
    color = command[1]
    physic = int(command[2])
    add_dwarf(name, color, physic)

    command = input()

show_result()