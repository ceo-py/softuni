matrix_row, matrix_col = [int(x) for x in input().split(", ")]
matrix, time_left = [], 16


def inside_matrix(row: int, col: int) -> bool:
    return 0 <= row < matrix_row and 0 <= col < matrix_col


def directions(direction: str) -> tuple:
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1),
    }.get(direction)


def create_matrix() -> tuple:
    c_row, c_col = 0, 0
    for row in range(matrix_row):
        matrix.append(list(input()))
        if "C" not in matrix[row]:
            continue
        c_row = row
        c_col = matrix[row].index("C")
    return c_row, c_col


c_row, c_col = create_matrix()


def step_in_matrix(direction: str) -> tuple:
    row, col = [
        a + b for a, b in zip((c_row, c_col), directions(direction))]

    if not inside_matrix(row, col):
        return (c_row, c_col, matrix[c_row][c_col])
    return (row, col, matrix[row][col])


while time_left > 0:

    command = input()

    if matrix[c_row][c_col] == "B" and command == "defuse":
        time_left -= 4

        if time_left >= 0:
            print("Counter-terrorist wins!")
            print(f"Bomb has been defused: {time_left} second/s remaining.")
            matrix[c_row][c_col] = "D"
        elif time_left < 0:
            matrix[c_row][c_col] = "X"
            print("Terrorists win!")
            print("Bomb was not defused successfully!")
            print(f"Time needed: {abs(time_left)} second/s.")

        break

    elif command == "defuse":
        time_left -= 2
        continue

    time_left -= 1
    c_row, c_col, step_on = step_in_matrix(command)

    if step_on == "T":
        matrix[c_row][c_col] = "*"
        print("Terrorists win!")
        break
else:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print("Time needed: 0 second/s.")

[print(*row, sep="") for row in matrix]
