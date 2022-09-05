from collections import deque

MATRIX_SIZE, matrix, rouver_row, rouver_col = 6, [], 0, 0
for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    if "E" in matrix[row]:
        rouver_row = row
        rouver_col = matrix[row].index("E")

commands = deque(input().split(", "))
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
found_materials = {"Water": False, "Concrete": False, "Metal": False}
borders, alive_rover = ((-1, 5), (6, 0)), [True]


def movement(row, col, direction):
    new_positions = [row + directions[direction][0], col + directions[direction][1]]
    for pos in range(len(new_positions)):
        for out_of_border, return_to_other_side_of_border in borders:
            if new_positions[pos] == out_of_border:
                new_positions[pos] = return_to_other_side_of_border
    return new_positions[0], new_positions[1]


def getting_materials(row, col, material):
    found_materials[material] = True
    print(f"{material} deposit found at ({row}, {col})")


def rock(row, col, _):
    print(f"Rover got broken at ({row}, {col})")
    alive_rover[0] = False


information = {"W": [getting_materials, "Water"], "M": [getting_materials, "Metal"],
               "C": [getting_materials, "Concrete"], "R": [rock, "_"]}

while commands and alive_rover[0]:
    direction = commands.popleft()
    rouver_row, rouver_col = movement(rouver_row, rouver_col, direction)
    rouver_step_field = matrix[rouver_row][rouver_col]
    if rouver_step_field != "-":
        information[rouver_step_field][0](rouver_row, rouver_col, information[rouver_step_field][1])

if all(found_materials.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
