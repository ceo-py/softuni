targets = [int(n) for n in input().split()]

how_long_index = len(targets)


def shoot_command(index, power):
    if index < how_long_index:
        targets[index] += - power
        if targets[index] <= 0:
            del targets[index]


def add_command(index, value):
    if index < how_long_index:
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_command(index, radius):
    condition_strike = [how_long_index > index, how_long_index > index + radius,
                        how_long_index > (index - radius) >= 0]
    if all(condition_strike):
        del targets[abs(index - radius):(index + radius + 1)]
    else:
        print("Strike missed!")


command = input()

while command != "End":
    command = command.split()
    type_command = command[0]
    index_command = int(command[1])
    value_command = int(command[2])

    if type_command == "Shoot":
        shoot_command(index_command, value_command)
    elif type_command == "Add":
        add_command(index_command, value_command)
    elif type_command == "Strike":
        strike_command(index_command, value_command)
    command = input()


print(*targets, sep="|")
