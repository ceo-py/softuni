def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True


def check_wall(row, col):
    if lab[row][col] == "#":
        return True


def check_already_visit(row, col):
    if lab[row][col] == "v":
        return True


def find_exit(row, col):
    if row == 0 or row == len(lab) - 1 or col == 0 or col == len(lab[0]):
        return True


def find_starting_point():
    for pos_row, row in enumerate(lab):
        for pos_col, col in enumerate(row):
            if col == "k":
                return pos_row, pos_col


def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col) or check_already_visit(row, col):
        return

    path_steps.append(1)

    if find_exit(row, col):
        max_len_path.append(sum(path_steps))

    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)  # check right
    find_the_lab_path(row, col - 1, lab)  # check left
    find_the_lab_path(row + 1, col, lab)  # check up
    find_the_lab_path(row - 1, col, lab)  # check down
    lab[row][col] = " "

    path_steps.pop()


row = int(input())
lab = []
path_steps = []
max_len_path = []
for _ in range(row):
    lab.append(list(input()))
col = len(lab[0])
start_row, start_col = find_starting_point()

find_the_lab_path(start_row, start_col, lab)

if max_len_path:
    print(f"Kate got out in {max(max_len_path)} moves")
else:
    print("Kate cannot get out")









# def find_position(maze):
#     position = []
#     for row in range(len(maze)):
#         for el in maze[row]:
#             if el == 'k':
#                 position.append(row)
#                 position.append(maze[row].find('k'))
#                 return position
#
#
# def next_free_spot(maze):
#     free_spots = []
#
#     for row in range(len(maze)):
#         for el in range(len(maze[row])):
#             tmp = []
#             if maze[row][el] == ' ':
#                 tmp.append(row)
#                 tmp.append(el)
#                 free_spots.insert(0, tmp)
#
#     return free_spots
#
#
# def find_path(position, next_free, maze):
#     is_blocked = True
#     step = 0
#     moves = 0
#
#     while step < len(next_free):
#         x1 = next_free[step][0]
#         x2 = next_free[step][1]
#         temp = []
#         temp.append(x1)
#         temp.append(x2)
# # moving left
#         if temp[0] == position[0] and position[1] - temp[1] == 1:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# # moving right
#         elif temp[0] == position[0] and temp[1] - position[1] == 1:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# # moving down
#         elif temp[0] - position[0] == 1 and position[1] == temp[1]:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
# # moving up
#         elif position[0] - temp[0] == 1 and position[1] == temp[1]:
#             position = temp
#             moves += 1
#             next_free.pop(step)
#             step = 0
#
#
#         else:
#
#             step += 1
#
#     if position[0] == 0 or position[0] == (len(maze) -1) or position[1] == 0 or position[1] == len(maze[0]):
#         return f'Kate got out in {moves + 1} moves'
#     return f'Kate cannot get out'
#
# m_rows = int(input())
# maze = []
# moves = 0
# free_space = True
# for row in range(m_rows):
#     maze.append(input())
# position = find_position(maze)
# next_free = next_free_spot(maze)
# movement = find_path(position, next_free, maze)
# print(movement)
#



#
# import queue
#
# maze_rows = int(input())
# maze = []
# way_out = []
# for _ in range(maze_rows):
#     maze.append([x for x in input()])
#
#
# def find_start_point(maze, point_start):
#     for i, row in enumerate(maze):
#         for j, value in enumerate(row):
#             if point_start == value:
#                 return i, j
#
#     return None
#
#
# def find_end_point(maze, point_end):
#     for i, row in enumerate(maze):
#         for j, value in enumerate(row):
#             if (i == 0 or i == maze_rows - 1) and point_end == value:
#                 return i, j
#
#     return None
#
#
# def find_path(maze):
#     global way_out
#     start = "k"
#     end = find_end_point(maze, " ")
#     start_pos = find_start_point(maze, start)
#     q = queue.Queue()
#     q.put((start_pos, [start_pos]))
#     visited = set()
#
#     while not q.empty():
#         current_pos, path = q.get()
#         row, col = current_pos
#         if current_pos == end:
#             way_out = path
#             return path
#
#         neighbors = find_neighbors(maze, row, col)
#         for neighbor in neighbors:
#             if neighbor in visited:
#                 continue
#
#             r, c = neighbor
#             if maze[r][c] == "#":
#                 continue
#
#             new_path = path + [neighbor]
#             q.put((neighbor, new_path))
#             visited.add(neighbor)
#
#
# def find_neighbors(maze, row, col):
#     neighbors = []
#     if row > 0:  # UP
#         neighbors.append((row - 1, col))
#     if row + 1 < len(maze):  # DOWN
#         neighbors.append((row + 1, col))
#     if col > 0:  # LEFT
#         neighbors.append((row, col - 1))
#     if col + 1 < len(maze[0]):  # RIGHT
#         neighbors.append((row, col + 1))
#
#     return neighbors
#
#
# find_path(maze)
# if way_out:
#     print(f"Kate got out in {len(way_out)} moves")
# else:
#     print("Kate cannot get out")
#
#
