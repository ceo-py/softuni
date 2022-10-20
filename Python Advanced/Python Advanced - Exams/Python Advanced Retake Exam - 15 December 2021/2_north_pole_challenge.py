rows, cols = [int(x) for x in input().split(", ")]

s_row, s_col, matrix, decorations, gifts, cookies, collected_all = 0, 0, [], 0, 0, 0, False

for row in range(rows):
    matrix.append(input().split())
    if "Y" in matrix[row]:
        s_row, s_col = row, matrix[row].index("Y")
        matrix[row][s_col] = "x"

command = input()
while command != "End" and not collected_all:
    direction, steps = [x if x.isalpha() else int(x) for x in command.split("-")]
    for step in range(steps):

        if direction == "up":
            s_row -= 1
        elif direction == "down":
            s_row += 1
        elif direction == "left":
            s_col -= 1
        elif direction == "right":
            s_col += 1

        if s_row == rows:
            s_row = 0
        elif s_row == -1:
            s_row = rows - 1

        elif s_col == cols:
            s_col = 0
        elif s_col == -1:
            s_col = cols - 1

        step_on = matrix[s_row][s_col]

        if step_on == "D":
            decorations += 1

        elif step_on == "G":
            gifts += 1

        elif step_on == "C":
            cookies += 1

        matrix[s_row][s_col] = "x"

        if any([x != "." and x != "x" for row_ in matrix for x in row_]):
            continue
        else:
            collected_all = True
            break

    if not collected_all:
        command = input()


matrix[s_row][s_col] = "Y"
if collected_all:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(*row) for row in matrix]



#
#
#
# rows, cols = [int(x) for x in input().split(", ")]
# matrix, santa_row, santa_col, items, keys = [], 0, 0, \
#     {"Christmas decorations": [0, 0], "Gifts": [0, 0], "Cookies": [0, 0]}\
#     , {"D": "Christmas decorations", "G": "Gifts", "C": "Cookies"}
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
#
# for row in range(rows):
#     matrix.append(input().split())
#     items["Christmas decorations"][0] += matrix[row].count("D")
#     items["Gifts"][0] += matrix[row].count("G")
#     items["Cookies"][0] += matrix[row].count("C")
#     if "Y" in matrix[row]:
#         santa_row, santa_col = row, matrix[row].index("Y")
#
#
# def check_traverse(*args):
#     row, col = args[0]
#     for c_row, new_row in ((-1, rows - 1), (rows, 0)):
#         if c_row == row:
#             row = new_row
#     for c_col, new_col in ((-1, cols - 1), (cols, 0)):
#         if c_col == col:
#             col = new_col
#     return row, col
#
#
# def moving_step(row, col, direction):
#     return row + directions[direction][0], col + directions[direction][1]
#
#
# def santo_on_the_move(row, col, direction, steps):
#     for step in range(steps):
#         step_row, step_col = check_traverse(moving_step(row, col, direction))
#         found_symbol = matrix[step_row][step_col]
#         if found_symbol not in ".x":
#             items[keys[found_symbol]][0] -= 1
#             items[keys[found_symbol]][1] += 1
#         matrix[row][col] = "x"
#         matrix[step_row][step_col] = "Y"
#         row, col = step_row, step_col
#         check_for_merry_christmas()
#     return row, col
#
#
# def check_for_merry_christmas():
#     if sum(x for x, _ in items.values()) == 0:
#         print("Merry Christmas!")
#         show_result()
#
#
# def show_result():
#     print("You've collected:")
#     for key, (_, value) in items.items():
#         if key != "keys":
#             print(f"- {value} {key}")
#     [print(*matrix[row]) for row in range(rows)]
#     exit()
#
#
# command = input()
#
# while command != "End":
#     position, steps = [int(x) if x.isdigit() else x for x in command.split("-")]
#     santa_row, santa_col = santo_on_the_move(santa_row, santa_col, position, steps)
#     command = input()
#
# show_result()
