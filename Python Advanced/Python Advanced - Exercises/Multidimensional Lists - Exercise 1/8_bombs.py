matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

for row, col in [[int(n) for n in x.split(",")] for x in input().split(" ")]:
    if matrix[row][col] <= 0: continue
    bomb_damage, matrix[row][col] = matrix[row][col], 0
    for row_pos, col_pos in ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)):
        if 0 <= row + row_pos < len(matrix) and 0 <= col + col_pos < len(matrix[0]):
            if matrix[row + row_pos][col + col_pos] > 0: matrix[row + row_pos][col + col_pos] -= bomb_damage

alive_cells = [num for row in range(len(matrix)) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
[print(*matrix[row]) for row in range(len(matrix))]





# rows = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# bombs_coordinates = [int(x) for x in input().replace(" ", ",").split(",")]
# cols, alive_cells, movement_explosion = len(matrix[0]), [], {
#     "up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0],
#     "top left diagonal": [-1, -1], "bottom left diagonal": [-1, 1],
#     "top right diagonal": [1, -1], "bottom right diagonal": [1, 1]}
#
# for i in range(0, len(bombs_coordinates), 2):
#     row, col = bombs_coordinates[i], bombs_coordinates[i + 1]
#     if matrix[row][col] > 0:
#         bomb_damage, matrix[row][col] = matrix[row][col], 0
#         for ind in movement_explosion:
#             row_movement, col_movement = row + movement_explosion[ind][0], col + movement_explosion[ind][1]
#             if 0 <= row_movement < rows and 0 <= col_movement < cols:
#                 if matrix[row_movement][col_movement] > 0:
#                     matrix[row_movement][col_movement] -= bomb_damage
#
# alive_cells = [num for row in range(len(matrix)) for num in matrix[row] if num > 0]
# print(f"Alive cells: {len(alive_cells)}\nSum: {sum(alive_cells)}")
# [print(*matrix[row], sep=" ") for row in range(len(matrix))]
#
#
#
#






#
#
# rows = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# bombs_coordinates = [int(x) for x in input().replace(" ", ",").split(",")]
# cols, alive_cells = len(matrix[0]), []
#
#
# def check_valid_index(row, col):
#     if 0 <= row < rows and 0 <= col < cols:
#         return True
#
#
# def explode(row, col, bomb_damage):
#     if matrix[row][col] > 0:
#         matrix[row][col] -= bomb_damage
#
#
# movement_explosion = {
#     "up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0],
#     "top left diagonal": [-1, -1], "bottom left diagonal": [-1, 1],
#     "top right diagonal": [1, -1], "bottom right diagonal": [1, 1]}
#
#
# for i in range(0, len(bombs_coordinates), 2):
#     row, col = bombs_coordinates[i], bombs_coordinates[i + 1]
#     if matrix[row][col] > 0:
#         bomb_damage, matrix[row][col] = matrix[row][col], 0
#         for ind in movement_explosion:
#             row_movement, col_movement = movement_explosion[ind]
#             if check_valid_index(row + row_movement, col + col_movement):
#                 explode(row + row_movement, col + col_movement, bomb_damage)
#
# for row in range(len(matrix)):
#     for num in matrix[row]:
#         if num > 0:
#             alive_cells.append(num)
#
# print(f"Alive cells: {len(alive_cells)}")
# print(f"Sum: {sum(alive_cells)}")
# for row in range(len(matrix)):
#     print(*matrix[row], sep=" ")
#
#
#
#






#
# rows = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# bombs_coordinates = [int(x) for x in input().replace(" ", ",").split(",")]
# cols = len(matrix[0])
# bomb_row = bombs_coordinates[::2]
# bomb_col = bombs_coordinates[1::2]
# alive_cells = []
#
#
# def check_valid_index(row, col):
#     if 0 <= row < rows and 0 <= col < cols:
#         return True
#
#
# def explode(row, col, bomb_damage):
#     if matrix[row][col] > 0:
#         matrix[row][col] -= bomb_damage
#
#
# movement_explosion = [0, -1, 0, 1, -1, 0, 1, 0, -1, -1, -1, 1, 1, -1, 1, 1]
# row_movement = movement_explosion[::2]
# col_movement = movement_explosion[1::2]
# for i in range(len(bomb_row)):
#     row, col = bomb_row[i], bomb_col[i]
#     if matrix[row][col] > 0:
#         bomb_damage, matrix[row][col] = matrix[row][col], 0
#         for ind in range(len(row_movement)):
#             if check_valid_index(row + row_movement[ind], col + col_movement[ind]):
#                 explode(row + row_movement[ind], col + col_movement[ind], bomb_damage)
#
# for row in range(len(matrix)):
#     for num in matrix[row]:
#         if num > 0:
#             alive_cells.append(num)
#
# print(f"Alive cells: {len(alive_cells)}")
# print(f"Sum: {sum(alive_cells)}")
# for row in range(len(matrix)):
#     print(*matrix[row], sep=" ")
