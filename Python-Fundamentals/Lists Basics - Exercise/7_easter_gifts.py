names_of_gifts = input().split(" ")


command = input()
while command != "No Money":
    if "OutOfStock" in command:
        out_of_stock = command.split()
        for i, name in enumerate(names_of_gifts):
            if out_of_stock[-1] == name:
                names_of_gifts[i] = "None"

    elif "Required" in command:
        required_gift = command.split()
        length = len(names_of_gifts)
        if length > int(required_gift[-1]) >= 0:
            names_of_gifts[int(required_gift[-1])] = required_gift[1]

    elif "JustInCase" in command:
        just_in_case = command.split()
        names_of_gifts[-1] = just_in_case[-1]
    command = input()

print(" ".join(x for x in names_of_gifts if x != "None"))
