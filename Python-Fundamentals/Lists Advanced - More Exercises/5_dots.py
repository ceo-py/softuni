def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True


def check_wall(row, col):
    if lab[row][col] in "-–":
        return True


def check_already_visit(row, col):
    if lab[row][col] == "v":
        return True


def find_exit(row, col):
    if lab[row][col] == ".":
        return True


def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col) or check_already_visit(row, col):
        return

    path_steps.append(1)

    if find_exit(row, col):
        max_connected_points.append(sum(path_steps))

    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)  # check right
    find_the_lab_path(row, col - 1, lab)  # check left
    find_the_lab_path(row + 1, col, lab)  # check up
    find_the_lab_path(row - 1, col, lab)  # check down


row = int(input())
lab = []
max_connected_points = [0]
for _ in range(row):
    lab.append(list(input().split()))
col_range = len(lab[0])

for row in range(len(lab)):
    for col in range(col_range):
        path_steps = []
        if not check_wall(row, col):
            find_the_lab_path(row, col, lab)


print(max(max_connected_points))









#
#
#
# n = int(input())
# matrix_main = []
#
# for _ in range(n):
#     matrix_main.append(input().split())
#
# m = len(matrix_main[0])
#
# # stores information about  which cell
# # are already visited in a particular BFS
# visited = [[0 for j in range(m)] for i in range(n)]
#
# # result stores the final result grid
# result = [[0 for j in range(m)] for i in range(n)]
#
# # stores the count of cells in the largest
# # connected component
# COUNT = 0
#
#
# # Function checks if a cell is valid i.e it
# # is inside the grid and equal to the key
# def is_valid(x, y, key, matrix_main):
#     if (x < n and y < m and x >= 0 and y >= 0):
#         if (visited[x][y] == 0 and matrix_main[x][y] == key):
#             return True
#         else:
#             return False
#
#     else:
#         return False
#
#
# # BFS to find all cells in
# # connection with key = input[i][j]
# def BFS(x, y, i, j, matrix_main):
#     global COUNT
#
#     # terminating case for BFS
#     if (x != y) or x != ".":
#         return
#     #
#     # if x != ".":
#     #     return
#
#
#     visited[i][j] = 1
#     COUNT += 1
#
#     # x_move and y_move arrays
#     # are the possible movements
#     # in x or y direction
#     x_move = [0, 0, 1, -1]
#     y_move = [1, -1, 0, 0]
#
#     # checks all four points connected with input[i][j]
#     for u in range(4):
#
#         if (is_valid(i + y_move[u], j + x_move[u], x, matrix_main)):
#             BFS(x, y, i + y_move[u], j + x_move[u], matrix_main)
#
#
# # called every time before a BFS
# # so that visited array is reset to zero
# def reset_visited():
#     for i in range(n):
#         for j in range(m):
#             visited[i][j] = 0
#
#
# # If a larger connected component
# # is found this function is called
# # to store information about that component.
# def reset_result(key, matrix_main):
#     for i in range(n):
#         for j in range(m):
#             if (visited[i][j] != 0 and matrix_main[i][j] == key):
#                 result[i][j] = visited[i][j]
#             else:
#                 result[i][j] = 0
#
#
# # function to print the result
# def print_result(res):
#     print(res)
#
#
# # function to calculate the largest connected
# # component
# def computeLargestConnectedGrid(matrix_main):
#     global COUNT
#     current_max = -10000000000
#
#     for i in range(n):
#         for j in range(m):
#             reset_visited()
#             COUNT = 0
#
#             # checking cell to the right
#             if (j + 1 < m):
#                 BFS(matrix_main[i][j], matrix_main[i][j + 1], i, j, matrix_main)
#
#             # updating result
#             if (COUNT >= current_max):
#                 current_max = COUNT
#                 reset_result(matrix_main[i][j], matrix_main)
#
#             reset_visited();
#             COUNT = 0;
#
#             # checking cell downwards
#             if (i + 1 < n):
#                 BFS(matrix_main[i][j], matrix_main[i + 1][j], i, j, matrix_main)
#
#             # updating result
#             if (COUNT >= current_max):
#                 current_max = COUNT
#                 reset_result(matrix_main[i][j], matrix_main)
#
#     print_result(current_max)
#
#
# computeLargestConnectedGrid(matrix_main)
#
