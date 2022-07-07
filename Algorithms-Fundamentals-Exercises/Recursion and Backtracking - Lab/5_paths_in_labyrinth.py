row = int(input())
col = int(input())

lab = []

for _ in range(row):
    lab.append([x for x in input()])

lab_directions = ""


def lab_borders(row, col, lab):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True


def find_exit(row, col, lab):
    if lab[row][col] == "e":
        return True


def find_wall(row, col, lab):
    if lab[row][col] == "*":
        return True


def visited_path(row, col, lab):
    if lab[row][col] == "v":
        return True


def find_lab_path(row, col, lab, direction):
    global lab_directions
    if lab_borders(row, col, lab) or find_wall(row, col, lab) or visited_path(row, col, lab):
        return

    lab_directions += direction

    if find_exit(row, col, lab):
        print(lab_directions)
    else:

        lab[row][col] = "v"
        find_lab_path(row + 1, col, lab, "D")
        find_lab_path(row - 1, col, lab, "U")
        find_lab_path(row, col + 1, lab, "R")
        find_lab_path(row, col - 1, lab, "L")
        lab[row][col] = "-"
    lab_directions = lab_directions[:-1]


find_lab_path(0, 0, lab, "")



# row = int(input())
# col = int(input())
#
# lab = []
#
# for _ in range(row):
#     lab.append([x for x in input()])
#
#
# def lab_borders(row, col, lab):
#     if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
#         return True
#
#
# def find_exit(row, col, lab):
#     if lab[row][col] == "e":
#         return True
#
#
# def find_wall(row, col, lab):
#     if lab[row][col] == "*":
#         return True
#
#
# def visited_path(row, col, lab):
#     if lab[row][col] == "v":
#         return True
#
#
# def find_lab_path(row, col, lab, direction, path):
#     if lab_borders(row, col, lab) or find_wall(row, col, lab) or visited_path(row, col, lab):
#         return
#
#     path.append(direction)
#
#     if find_exit(row, col, lab):
#         print(*path, sep="")
#     else:
#         lab[row][col] = "v"
#         find_lab_path(row + 1, col, lab, "D", path)
#         find_lab_path(row - 1, col, lab, "U", path)
#         find_lab_path(row, col + 1, lab, "R", path)
#         find_lab_path(row, col - 1, lab, "L", path)
#         lab[row][col] = "-"
#     path.pop()
#
#
# find_lab_path(0, 0, lab, "", [])
