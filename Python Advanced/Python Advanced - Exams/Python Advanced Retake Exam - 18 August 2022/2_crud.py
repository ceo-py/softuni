MATRIX_SIZE = 6
matrix = [input().split() for _ in range(MATRIX_SIZE)]
row_position, col_position = [int(x) for x in input().replace("(", "").replace(")", "").split(",")]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def add_step(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


def create(args):
    step_row, step_col = add_step(row_position, col_position, args[0])
    if matrix[step_row][step_col] == ".":
        matrix[step_row][step_col] = args[1]
    return step_row, step_col


def update(args):
    step_row, step_col = add_step(row_position, col_position, args[0])
    if matrix[step_row][step_col].isalpha() or matrix[step_row][step_col][-1].isdigit():
        matrix[step_row][step_col] = args[1]
    return step_row, step_col


def delete(args):
    step_row, step_col = add_step(row_position, col_position, args[0])
    if matrix[step_row][step_col].isalpha() or matrix[step_row][step_col][-1].isdigit():
        matrix[step_row][step_col] = "."
    return step_row, step_col


def read(args):
    step_row, step_col = add_step(row_position, col_position, args[0])
    if matrix[step_row][step_col].isalpha() or matrix[step_row][step_col][-1].isdigit():
        print(matrix[step_row][step_col])
    return step_row, step_col


commands = {
    "Create": create,
    "Update": update,
    "Read": read,
    "Delete": delete
}
command = input()

while command != "Stop":
    command_type, *info = command.split(", ")
    row_position, col_position = commands[command_type](info)
    command = input()

[print(*matrix[row]) for row in range(MATRIX_SIZE)]