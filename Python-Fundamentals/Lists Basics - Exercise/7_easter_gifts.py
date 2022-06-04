names_of_gifts = input().split(" ")


command = input()
while command != "No Money":
    command_type, *other_info = command.split()
    if "OutOfStock" in command_type:
        for i, name in enumerate(names_of_gifts):
            if other_info[-1] == name:
                names_of_gifts[i] = "None"
    elif "Required" in command_type:
        length = len(names_of_gifts)
        if length > int(other_info[-1]) >= 0:
            names_of_gifts[int(other_info[-1])] = other_info[0]
    elif "JustInCase" in command_type:
        names_of_gifts[-1] = other_info[-1]
    command = input()

print(" ".join(x for x in names_of_gifts if x != "None"))
