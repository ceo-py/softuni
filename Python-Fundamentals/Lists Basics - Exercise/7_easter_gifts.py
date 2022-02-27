names_of_gifts = input().split(" ")

out_of_stock = list()
required_gift = list()
just_in_case = list()

while True:
    command = input()
    if command == "No Money":
        break

    elif "OutOfStock" in command:
        out_of_stock.clear()
        out_of_stock = command.split(" ")
        i = 0
        for name in names_of_gifts:
            if out_of_stock[-1] == name:
                names_of_gifts[i] = "None"
            i += 1

    elif "Required" in command:
        required_gift.clear()
        required_gift = command.split(" ")
        length = int(len(names_of_gifts))
        if int(required_gift[-1]) < length and int(required_gift[-1]) >= 0:
            names_of_gifts[int(required_gift[-1])] = required_gift[1]

    elif "JustInCase" in command:
        just_in_case.clear()
        just_in_case = command.split(" ")
        names_of_gifts[-1] = just_in_case[-1]

for name in names_of_gifts:
    if name != "None":
        print(name, end=" ")
