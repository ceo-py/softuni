rows = int(input())
snake_row, snake_col, lairs, matrix, food_quantity = 0, 0, [], [], [0]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
snake_is_alive = [True]

for row in range(rows):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        snake_row, snake_col = row, matrix[row].index("S")
    elif "B" in matrix[row]:
        lairs.append([row, matrix[row].index("B")])

cols = len(matrix[0])


def check_valid_index(row, col):
    return 0 <= row < rows and 0 <= col < cols


def snake_teleport(row, col):
    lairs.remove([row, col])
    return lairs[0][0], lairs[0][1]


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


def snake_step(row, col, direction):
    new_row, new_col = movement(row, col, direction)
    if check_valid_index(new_row, new_col):
        if matrix[new_row][new_col] == "B":
            matrix[new_row][new_col] = "."
            new_row, new_col = snake_teleport(new_row, new_col)

        elif matrix[new_row][new_col] == "*":
            food_quantity[0] += 1
        matrix[row][col] = "."
        matrix[new_row][new_col] = "S"
        return new_row, new_col
    snake_is_alive[0] = False
    matrix[row][col] = "."
    return row, col


while food_quantity[0] < 10 and snake_is_alive[0]:
    direction = input()
    if direction in directions:
        snake_row, snake_col = snake_step(snake_row, snake_col, direction)

if snake_is_alive[0]:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity[0]}")
[print(*matrix[row], sep="") for row in range(rows)]