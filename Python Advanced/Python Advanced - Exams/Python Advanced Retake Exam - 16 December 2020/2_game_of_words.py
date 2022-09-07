player_info = {"Word": input()}
MATRIX_SIZE = int(input())
player_row, player_col, matrix = 0, 0, []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(MATRIX_SIZE):
    matrix.append(list(input()))
    if "P" in matrix[row]:
        player_row, player_col = row, matrix[row].index("P")
        matrix[player_row][player_col] = "-"


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


def check_where_he_steps(row, col, direction):
    new_row, new_col = movement(row, col, direction)
    if check_valid_index(new_row, new_col):
        symbol = matrix[new_row][new_col]
        if symbol != "-":
            player_info["Word"] += symbol
            matrix[new_row][new_col] = "-"
        return new_row, new_col
    player_info["Word"] = player_info["Word"][:-1]
    return row, col


number_of_commands = int(input())
for com in range(number_of_commands):
    command = input()
    if command not in directions:
        continue
    player_row, player_col = check_where_he_steps(player_row, player_col, command)

matrix[player_row][player_col] = "P"
print(player_info["Word"])
[print(*row, sep="") for row in matrix]


'''
4
P---
Mark
-l-y
--e-
4
down
right
right
right
'''