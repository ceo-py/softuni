
def correct_lab_bounds(row, col):
    return row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0])


def check_wall(row, col):
    return lab[row][col] in "-–"


def check_already_visit(row, col):
    return lab[row][col] == "v"


def find_exit(row, col):
    return lab[row][col] == "."


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










# from copy import deepcopy
#
#
# def count_dots(grid):
#     dots = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '.']
#     list_of_groups = []
#
#     for dot in dots:
#         group = set()
#         group.add(dot)
#
#         for _dot in dots:
#             if (dot[0] == _dot[0] and (dot[1] == _dot[1] + 1 or dot[1] == _dot[1] - 1)) \
#                     or (dot[1] == _dot[1] and (dot[0] == _dot[0] + 1 or dot[0] == _dot[0] - 1)):
#                 group.add(_dot)
#         list_of_groups.append(group)
#
#     return dots, list_of_groups
#
#
# def extract_groups(dots, list_of_groups):
#     change = False
#     while change is False:
#         change = False
#
#         for g in range(len(deepcopy(list_of_groups))):
#             for _g in range(len(list_of_groups)):
#
#                 if list_of_groups[g] is not None and list_of_groups[_g] is not None:
#                     if list_of_groups[g] != list_of_groups[_g] and not list_of_groups[g].isdisjoint(list_of_groups[_g]):
#                         list_of_groups[g] = list_of_groups[g] | list_of_groups[_g]
#                         list_of_groups[_g] = None
#                         change = True
#
#         list_of_groups = [group for group in list_of_groups if group != None]
#
#     return list_of_groups
#
#
# def main():
#     grid = []
#     for _ in range(int(input())):
#         grid.append(input().split())
#
#     dots, list_of_groups = count_dots(grid)
#     groups = extract_groups(dots, list_of_groups)
#     the_group = max([len(group) for group in groups])
#     print(the_group)
#
#
# if __name__ == '__main__':
#     main()







#
# def dfs(i, j, n, m, grid, visited):
#     count = 0
#     if 0 <= i < n and 0 <= j < m and grid[i][j] == "." and not visited[i][j]:
#         visited[i][j] = True
#         count = 1 + dfs(i - 1, j, n, m, grid, visited) + dfs(i + 1, j, n, m, grid, visited) + dfs(i, j - 1, n, m, grid, visited) + dfs(i, j + 1, n, m, grid, visited)
#     return count
#
# def largest_connected_dots(n, grid):
#     m = len(grid[0])
#     max_dots = 0
#     for i in range(n):
#         for j in range(m):
#             if grid[i][j] == ".":
#                 visited = [[False for j in range(m)] for i in range(n)]
#                 max_dots = max(max_dots, dfs(i, j, n, m, grid, visited))
#     return max_dots
#
# n = int(input())
# grid = [input().split() for _ in range(n)]
#
# print(largest_connected_dots(n, grid))
#
#
#



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
