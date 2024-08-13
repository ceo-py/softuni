matrix_size = int(input())
matrix = []
player = {
    "possition": {
        "row": 0,
        "col": 0
    },
    "stars": 2
}


def create_matrix(matrix_size: int) -> None:
    for row in range(matrix_size):
        matrix.append(list(input().split()))
        if "P" in matrix[row]:
            player["possition"]["row"] = row
            col = matrix[row].index("P")
            player["possition"]["col"] = col
            matrix[row][col] = "."


def directions(direction: str) -> tuple:
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }.get(direction)


def inside_matrix(row: int, col: int) -> bool:
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def player_move(direction: str) -> str:
    row, col = [
        a + b for a, b in zip(player["possition"].values(), directions(direction))
    ]

    if not inside_matrix(row, col):
        row, col = 0, 0

    step_on = matrix[row][col]
    if step_on == "#":
        return step_on

    player["possition"]["row"] = row
    player["possition"]["col"] = col

    return step_on


def show_matrix():
    row, col = player["possition"].values()
    matrix[row][col] = "P"
    print(f"Your final position is [{row}, {col}]")
    [print(" ".join(row)) for row in matrix]


create_matrix(matrix_size)

while player["stars"] != 0:
    direction = input()
    step_on = player_move(direction)

    if step_on == "*":
        player["stars"] += 1
        matrix[player["possition"]["row"]][player["possition"]["col"]] = "."

        if player["stars"] == 10:
            print("You won! You have collected 10 stars.")
            break

    elif step_on == "#":
        player["stars"] -= 1

else:
    print("Game over! You are out of any stars.")

show_matrix()
