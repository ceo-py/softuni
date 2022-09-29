from collections import deque

MATRIX_SIZE = int(input())
commands = deque(input().split())

coal = 0
collected_coal = 0
start_row, start_col = 0, 0
matrix = []
movement = {
    "up": (-1, 0), "down": (1, 0),
    "left": (0, -1), "right": (0, 1)
}

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    coal += matrix[row].count("c")
    if "s" in matrix[row]:
        start_row, start_col = row, matrix[row].index("s")

while commands:
    direction = commands.popleft()
    moving_row, moving_col = start_row + movement[direction][0], start_col + movement[direction][1]
    if not 0 <= moving_row < MATRIX_SIZE or not 0 <= moving_col < MATRIX_SIZE:
        continue

    symbol = matrix[moving_row][moving_col]

    if symbol == "e":
        print(f"Game over! {moving_row, moving_col}")
        break

    if symbol == "c":
        matrix[moving_row][moving_col] = "*"
        collected_coal += 1

    if collected_coal == coal:
        print(f"You collected all coal! {moving_row, moving_col}")
        break

    start_row, start_col = moving_row, moving_col
else:
    print(f"{coal - collected_coal} pieces of coal left. {moving_row, moving_col}")




# field_numbers = int(input())
# commands = input().split()
# mine_field = [input().split() for _ in range(field_numbers)]
#
# command_movement = {
#     "up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]
# }
#
#
# def find_starting_position():
#     total_coal = 0
#     for row in range(field_numbers):
#         if "s" in mine_field[row]:
#             row_find, col_find = row, mine_field[row].index("s")
#         total_coal += mine_field[row].count("c")
#     return row_find, col_find, total_coal
#
#
# row, col, total_coal = find_starting_position()
#
#
# def check_valid_index(col, row):
#     if 0 <= row < field_numbers and 0 <= col < len(mine_field[row]):
#         return True
#
#
# def end_route(col, row):
#     if mine_field[row][col] == "e":
#         print(f"Game over! ({row}, {col})")
#         exit()
#
#
# def coal_position(col, row, coal):
#     if mine_field[row][col] == "c":
#         mine_field[row][col] = "*"
#         coal -= 1
#     return coal
#
#
# def check_movement(col, row, coal):
#     end_route(col, row)
#     return col, row, coal_position(col, row, coal)
#
#
# for command in commands:
#     row_check, col_check = row + command_movement[command][0], col + command_movement[command][1]
#     if check_valid_index(col_check, row_check):
#         col, row, total_coal = check_movement(col_check, row_check, total_coal)
#         if total_coal == 0:
#             print(f"You collected all coal! ({row}, {col})")
#             break
# else:
#     print(f"{total_coal} pieces of coal left. ({row}, {col})")


# field_numbers = int(input())
# commands = input().split()
# mine_field = [input().split() for _ in range(field_numbers)]
#
#
# def find_starting_position():
#     total_coal = 0
#     for col in range(len(mine_field)):
#         if "s" in mine_field[col]:
#             colon = col
#             row = mine_field[col].index("s")
#         if "c" in mine_field[col]:
#             total_coal += mine_field[col].count("c")
#     return row, colon, total_coal
#
#
# col, row, total_coal = find_starting_position()
#
#
# def check_valid_index(col, row):
#     if 0 <= row < len(mine_field) and 0 <= col < len(mine_field[row]):
#         return True
#
#
# def end_of_route(col, row):
#     if mine_field[row][col] == "e":
#         print(f"Game over! ({row}, {col})")
#         exit()
#
#
# def coal_position(col, row, coal):
#     if mine_field[row][col] == "c":
#         mine_field[row][col] = "*"
#         coal -= 1
#     return coal
#
#
# def up(col, row, total_coal):
#     if check_valid_index(row - 1, col):
#         row -= 1
#         end_of_route(col, row)
#         total_coal = coal_position(col, row, total_coal)
#     return col, row, total_coal
#
#
# def down(col, row, total_coal):
#     if check_valid_index(row + 1, col):
#         row += 1
#         end_of_route(col, row)
#         total_coal = coal_position(col, row, total_coal)
#     return col, row, total_coal
#
#
# def left(col, row, total_coal):
#     if check_valid_index(row, col - 1):
#         col -= 1
#         end_of_route(col, row)
#         total_coal = coal_position(col, row, total_coal)
#     return col, row, total_coal
#
#
# def right(col, row, total_coal):
#     if check_valid_index(row, col + 1):
#         col += 1
#         end_of_route(col, row)
#         total_coal = coal_position(col, row, total_coal)
#     return col, row, total_coal
#
#
# command_dic = {
#     "up": up,
#     "down": down,
#     "left": left,
#     "right": right
#
# }
# for command in commands:
#     col, row, total_coal = command_dic[command](col, row, total_coal)
#     if total_coal == 0:
#         print(f"You collected all coal! ({row}, {col})")
#         break
# else:
#     print(f"{total_coal} pieces of coal left. ({row}, {col})")
#
#
