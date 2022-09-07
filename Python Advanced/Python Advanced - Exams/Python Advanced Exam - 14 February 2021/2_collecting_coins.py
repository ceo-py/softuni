from math import floor

rows = int(input())

cols, player_row, player_col, walls, matrix, my_path, player_info = 0, 0, 0, [], [], [], {"coins": 0, "alive": True}
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(rows):
    matrix.append(input().split())
    for col in range(len(matrix[0])):
        if matrix[row][col] == "P":
            cols = len(matrix[0])
            my_path.append([row, col])
            player_row, player_col = row, col
        elif matrix[row][col] == "X":
            walls.append((row, col))

borders = ((-1, rows - 1, rows, 0), (-1, cols - 1, cols, 0))


def check_for_traverse(row, col):
    for c_row in range(0, 4, 2):
        if borders[0][c_row] == row:
            row = borders[0][c_row + 1]
    for c_col in range(0, 4, 2):
        if borders[1][c_col] == col:
            col = borders[0][c_col + 1]
    return row, col


def movement(row, col, direction):
    return check_for_traverse(row + directions[direction][0], col + directions[direction][1])


def check_for_wall(row, col):
    if (row, col) in walls:
        player_info["alive"] = False
        return True


def add_coins(row, col):
    symbol = matrix[row][col]
    if symbol.isdigit():
        player_info["coins"] += int(symbol)
        matrix[row][col] = "-"


def check_where_he_steps(row, col, direction):
    movement_row, movement_col = movement(row, col, direction)
    my_path.append([movement_row, movement_col])
    if not check_for_wall(movement_row, movement_col):
        add_coins(movement_row, movement_col)
    return movement_row, movement_col


def show_result():
    print("Your path:")
    [print(row) for row in my_path]


while player_info["alive"] and player_info["coins"] < 100:
    direction = input()
    if direction in directions:
        player_row, player_col = check_where_he_steps(player_row, player_col, direction)

if player_info["alive"]:
    print(f"You won! You've collected {player_info['coins']} coins.")
else:
    print(f"Game over! You've collected {floor((player_info['coins'])/2)} coins.")

show_result()
