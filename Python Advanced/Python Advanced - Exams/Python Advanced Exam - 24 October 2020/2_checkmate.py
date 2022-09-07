MATRIX_SIZE = 8

matrix, queens_pos, king_row, king_col = [], [], 0, 0

# 0 index is column 1 index is row

directions = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "top left diagonal": (-1, -1), "bottom left diagonal": (-1, 1),
    "top right diagonal": (1, -1), "bottom right diagonal": (1, 1)}


for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    if "K" in matrix[row]:
        king_row, king_col = row, matrix[row].index("K")


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


for direction in directions:
    new_row, new_col = king_row, king_col
    for step in range(MATRIX_SIZE):
        new_row, new_col = movement(new_row, new_col, direction)
        if check_valid_index(new_row, new_col):
            if matrix[new_row][new_col] == "Q":
                queens_pos.append([new_row, new_col])
                break
        else:
            break

if queens_pos:
    [print(row) for row in queens_pos]
else:
    print("The king is safe!")





