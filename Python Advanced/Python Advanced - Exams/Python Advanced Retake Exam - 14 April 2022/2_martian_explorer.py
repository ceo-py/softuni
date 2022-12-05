from collections import deque

water, concrete, metal, row, col = 0, 0, 0, 0, 0
matrix = []
for row_ in range(6):
    matrix.append(input().split())
    if "E" in matrix[row_]:
        row, col = row_, matrix[row_].index("E")

commands = deque(input().split(', '))

while commands:
    command = commands.popleft()

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    for c_pos, n_pos in ((-1, 5), (6, 0)):
        if col == c_pos:
            col = n_pos
        if row == c_pos:
            row = n_pos

    step_on = matrix[row][col]

    if step_on == "W":
        water += 1
        print(f"Water deposit found at ({row}, {col})")
    elif step_on == "M":
        metal += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif step_on == "C":
        concrete += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif step_on == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if metal and water and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")









#
#
# from collections import deque
#
# matrix, rouver_info = [], {"position": {"row": 0, "col": 0}, "alive": True,
#                            "materials": {"Water": False, "Concrete": False, "Metal": False}, "borders": {-1: 5, 6: 0}}
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
#
# for row in range(6):
#     matrix.append(input().split())
#     if "E" in matrix[row]:
#         rouver_info["position"]["row"] = row
#         rouver_info["position"]["col"] = matrix[row].index("E")
#
# commands = deque(input().split(", "))
#
#
# def movement(row, col, direction):
#     new_positions = [row + directions[direction][0], col + directions[direction][1]]
#     for pos in range(len(new_positions)):
#         if new_positions[pos] in rouver_info["borders"]:
#             new_positions[pos] = rouver_info["borders"][new_positions[pos]]
#     return new_positions[0], new_positions[1]
#
#
# def getting_materials(row, col, material):
#     rouver_info["materials"][material] = True
#     print(f"{material} deposit found at ({row}, {col})")
#
#
# def rock(row, col, _):
#     print(f"Rover got broken at ({row}, {col})")
#     rouver_info["alive"] = False
#
#
# information = {"W": {"command": getting_materials, "material": "Water"},
#                "M": {"command": getting_materials, "material": "Metal"},
#                "C": {"command": getting_materials, "material": "Concrete"},
#                "R": {"command": rock, "material": "_"}}
#
# while commands and rouver_info["alive"]:
#     direction = commands.popleft()
#     rouver_info["position"]["row"], rouver_info["position"]["col"] = movement(rouver_info["position"]["row"],
#                                                                               rouver_info["position"]["col"], direction)
#     rouver_step_field = matrix[rouver_info["position"]["row"]][rouver_info["position"]["col"]]
#     if rouver_step_field != "-":
#         information[rouver_step_field]["command"](rouver_info["position"]["row"], rouver_info["position"]["col"],
#                                                   information[rouver_step_field]["material"])
#
# if all(rouver_info["materials"].values()):
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")

#
#
# from collections import deque
#
# MATRIX_SIZE, matrix, rouver_row, rouver_col = 6, [], 0, 0
# for row in range(MATRIX_SIZE):
#     matrix.append(input().split())
#     if "E" in matrix[row]:
#         rouver_row = row
#         rouver_col = matrix[row].index("E")
#
# commands = deque(input().split(", "))
# directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
# found_materials = {"Water": False, "Concrete": False, "Metal": False}
# borders, alive_rover = ((-1, 5), (6, 0)), [True]
#
#
# def movement(row, col, direction):
#     new_positions = [row + directions[direction][0], col + directions[direction][1]]
#     for pos in range(len(new_positions)):
#         for out_of_border, return_to_other_side_of_border in borders:
#             if new_positions[pos] == out_of_border:
#                 new_positions[pos] = return_to_other_side_of_border
#     return new_positions[0], new_positions[1]
#
#
# def getting_materials(row, col, material):
#     found_materials[material] = True
#     print(f"{material} deposit found at ({row}, {col})")
#
#
# def rock(row, col, _):
#     print(f"Rover got broken at ({row}, {col})")
#     alive_rover[0] = False
#
#
# information = {"W": (getting_materials, "Water"), "M": (getting_materials, "Metal"),
#                "C": (getting_materials, "Concrete"), "R": (rock, "_")}
#
# while commands and alive_rover[0]:
#     direction = commands.popleft()
#     rouver_row, rouver_col = movement(rouver_row, rouver_col, direction)
#     rouver_step_field = matrix[rouver_row][rouver_col]
#     if rouver_step_field != "-":
#         information[rouver_step_field][0](rouver_row, rouver_col, information[rouver_step_field][1])
#
# if all(found_materials.values()):
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")
