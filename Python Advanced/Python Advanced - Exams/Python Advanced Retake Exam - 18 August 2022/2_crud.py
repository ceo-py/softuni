'''
никакви проверки за позиция в матрицата или команди коректни
единственото правеното на командите

'''

matrix = [input().split() for _ in range(6)]

row, col = [int(x) for x in input()[1:-1].split(", ")]
# info = input()
# row, col = int(info[1]), int(info[-1])
# row, col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]

command = input()

while command != "Stop":
    command_type, direction, *value = command.split(", ")

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    step_on = matrix[row][col]

    if command_type == "Create" and step_on == ".":
        step_on = value[0]

    elif not step_on.isalnum():
        pass

    elif command_type == "Update":
        step_on = value[0]

    elif command_type == "Delete":
        step_on = "."

    elif command_type == "Read":
        print(step_on)

    matrix[row][col] = step_on
    command = input()

[print(*row) for row in matrix]








#
#
#
# MATRIX_SIZE = 6
# matrix = [input().split() for _ in range(MATRIX_SIZE)]
# row_position, col_position = [int(x) for x in input()[1:-1].split(",")]
# directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
#
#
# def add_step(row, col, direction):
#     return row + directions[direction][0], col + directions[direction][1]
#
#
# def number_or_letter():
#     return matrix[row_position][col_position].isalpha() or matrix[row_position][col_position].isdigit()
#
#
# def create(value):
#     if matrix[row_position][col_position] == ".":
#         matrix[row_position][col_position] = value
#
#
# def update(value):
#     matrix[row_position][col_position] = value
#
#
# def delete(_):
#     matrix[row_position][col_position] = "."
#
#
# def read(_):
#     print(matrix[row_position][col_position])
#
#
# commands = {
#     "Create": create,
#     "Update": update,
#     "Read": read,
#     "Delete": delete
# }
# command, commands_no_create = input(), tuple(commands.keys())[1:]
#
# while command != "Stop":
#     command_type, *info = command.split(", ")
#     row_position, col_position = add_step(row_position, col_position, info[0])
#     if command_type in commands_no_create:
#         if number_or_letter():
#             commands[command_type](info[-1])
#     else:
#         commands[command_type](info[-1])
#     command = input()
#
# [print(*matrix[row]) for row in range(MATRIX_SIZE)]
#
#
#
#
#










#
#
#
# MATRIX_SIZE = 6
# matrix = [input().split() for _ in range(MATRIX_SIZE)]
# row_position, col_position = [int(x) for x in input().replace("(", "").replace(")", "").split(",")]
# directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
#
#
# def add_step(row, col, direction):
#     return row + directions[direction][0], col + directions[direction][1]
#
#
# def create(args):
#     step_row, step_col = add_step(row_position, col_position, args[0])
#     if matrix[step_row][step_col] == ".":
#         matrix[step_row][step_col] = args[1]
#     return step_row, step_col
#
#
# def update(args):
#     step_row, step_col = add_step(row_position, col_position, args[0])
#     if matrix[step_row][step_col].isalpha() or matrix[step_row][step_col][-1].isdigit():
#         matrix[step_row][step_col] = args[1]
#     return step_row, step_col
#
#
# def delete(args):
#     step_row, step_col = add_step(row_position, col_position, args[0])
#     if matrix[step_row][step_col].isalpha() or matrix[step_row][step_col][-1].isdigit():
#         matrix[step_row][step_col] = "."
#     return step_row, step_col
#
#
# def read(args):
#     step_row, step_col = add_step(row_position, col_position, args[0])
#     if matrix[step_row][step_col].isalpha() or matrix[step_row][step_col][-1].isdigit():
#         print(matrix[step_row][step_col])
#     return step_row, step_col
#
#
# commands = {
#     "Create": create,
#     "Update": update,
#     "Read": read,
#     "Delete": delete
# }
# command = input()
#
# while command != "Stop":
#     command_type, *info = command.split(", ")
#     row_position, col_position = commands[command_type](info)
#     command = input()
#
# [print(*matrix[row]) for row in range(MATRIX_SIZE)]