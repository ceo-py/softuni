numbers = list(map(int, input().split()))
command = input()
while command != "Finish":
    command = command.split()
    command_name = command[0]
    command_value = int(command[1])
    if command_name == "Add":
        numbers.append(command_value)
    elif command_name == "Remove":
        numbers.remove(command_value)
    elif command_name == "Replace":
        replacement = int(command[2])
        if command_value in numbers:
            numbers[numbers.index(command_value)] = replacement
    elif command_name == "Collapse":
        numbers = [x for x in numbers if x >= command_value]
    command = input()
print(*numbers)