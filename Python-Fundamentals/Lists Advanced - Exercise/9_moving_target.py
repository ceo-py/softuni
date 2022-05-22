targets = [int(n) for n in input().split()]
command = input()


def Shoot(index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            del targets[index]


def Add(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        return "Invalid placement!"


def Strike(index, radius):
    if all([index - radius >= 0, index + radius < len(targets)]):
        del targets[index - radius:index + radius + 1]
    else:
        return "Strike missed!"


command_list = [Shoot, Add, Strike]
while command != "End":
    type_command, index_target, power_value_radius = command.split()
    for function in command_list:
        if function.__name__ == type_command:
            result_ = function(int(index_target), int(power_value_radius))
            if result_:
                print(result_)
            break
    command = input()

print(*targets, sep="|")

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
