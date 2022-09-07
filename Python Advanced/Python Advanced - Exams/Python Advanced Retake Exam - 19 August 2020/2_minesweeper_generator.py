MATRIX_SIZE = int(input())
bombs_number = int(input())

directions = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "top left diagonal": (-1, -1), "bottom left diagonal": (-1, 1),
    "top right diagonal": (1, -1), "bottom right diagonal": (1, 1)}
matrix = [[x for x in "0" * MATRIX_SIZE] for _ in range(MATRIX_SIZE)]
for bomb in range(bombs_number):
    bomb_row, bomb_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
    matrix[bomb_row][bomb_col] = "*"


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def check_for_bombs_in_range(row, col):
    current_sum = 0
    for moving_col, moving_row in directions.values():
        check_row, check_col = row + moving_row, col + moving_col
        if check_valid_index(check_row, check_col) and matrix[check_row][check_col] == "*":
            current_sum += 1
            matrix[row][col] = current_sum


for row in range(MATRIX_SIZE):
    for col in range(MATRIX_SIZE):
        if matrix[row][col] != "*":
            check_for_bombs_in_range(row, col)

[print(*matrix[row]) for row in range(MATRIX_SIZE)]
