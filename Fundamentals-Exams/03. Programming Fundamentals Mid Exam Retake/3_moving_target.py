targets = [int(x) for x in input().split()]
data_info = input()

while data_info != "End":
    command, index, value = [int(x) if x[-1].isdigit() else x for x in data_info.split()]
    valid_index = True
    if not 0 <= index < len(targets):
        valid_index = False

    elif command == "Shoot":
        targets[index] -= value
        if targets[index] <= 0:
            del targets[index]

    if command == "Add":
        if valid_index:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike" and valid_index:
        start_radius = index - value
        end_radius = index + value + 1
        if 0 <= start_radius < end_radius < len(targets):
            del targets[start_radius:end_radius]
        else:
            print("Strike missed!")
    data_info = input()

print(*targets, sep="|")



#
#
#
# targets = [int(n) for n in input().split()]
# command = input()
#
#
# def shoot_target(index, power):
#     if 0 <= index < len(targets):
#         targets[index] -= power
#         if targets[index] <= 0:
#             del targets[index]
#
#
# def add_target(index, value):
#     if 0 <= index < len(targets):
#         targets.insert(index, value)
#     else:
#         print("Invalid placement!")
#
#
# def strike_target(index, radius):
#     if all([index - radius >= 0, index + radius < len(targets)]):
#         del targets[index - radius:index + radius + 1]
#     else:
#         print("Strike missed!")
#
#
# while command != "End":
#     command = command.split()
#     type_command = command[0]
#     index_target = int(command[1])
#     power_value_radius = int(command[2])
#     if type_command == "Shoot":
#         shoot_target(index_target, power_value_radius)
#     elif type_command == "Add":
#         add_target(index_target, power_value_radius)
#     elif type_command == "Strike":
#         strike_target(index_target, power_value_radius)
#     command = input()
#
# print(*targets, sep="|")
