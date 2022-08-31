rows = int(input())
matrix = [[int(x) if x[-1].isdigit() else x for x in input().split()] for _ in range(rows)]

cols, result, directions = len(matrix[0]), {}, {
    "up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]
}


def find_starting_position():
    for row in range(rows):
        if "B" in matrix[row]:
            return row, matrix[row].index("B")


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols and matrix[row][col] != "X":
        return True


bunny_row, bunny_col = find_starting_position()


def movement():
    for direction, (row, col) in directions.items():
        bunny_move_row, bunny_move_col = bunny_row + row, bunny_col + col
        for jump in range(cols):
            if check_valid_index(bunny_move_row, bunny_move_col):
                result[direction] = result.get(direction, 0) + matrix[bunny_move_row][bunny_move_col]
                bunny_move_row, bunny_move_col = row + bunny_move_row, col + bunny_move_col
            else:
                break


movement()
if sum(result.values()) != 0:
    max_direction = max(result, key=result.get)
    print(max_direction)
    for path in range(cols):
        print_row, print_col = bunny_row + directions[max_direction][0], bunny_col + directions[max_direction][1]
        if check_valid_index(print_row, print_col):
            print(f"[{print_row}, {print_col}]")
            bunny_row, bunny_col = print_row, print_col
        else:
            break
    print(result[max_direction])


