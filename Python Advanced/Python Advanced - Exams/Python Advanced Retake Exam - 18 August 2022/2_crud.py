from collections import deque

seats = input().split(", ")
first_number = deque(int(x) for x in input().split(", "))
second_number = deque(int(x) for x in input().split(", "))

rotations, matched_seats = 0, []

while len(matched_seats) != 3 and rotations != 10:
    first_num = first_number.popleft()
    second_num = second_number.pop()
    rotations += 1

    letter = chr(first_num + second_num)
    found = False
    for seat in (f"{first_num}{letter}", f"{second_num}{letter}"):
        if seat in seats:
            matched_seats.append(seat)
            seats.remove(seat)
            found = True

    if found:
        continue

    first_number.append(first_num)
    second_number.appendleft(second_num)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")








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