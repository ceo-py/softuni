rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]
commands = input()

winner = False
movement = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}


def find_player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")


def player_alive(row, col):
    if matrix[row][col] == "B":
        show_result("dead")


def check_valid_index(row, col, player=False):
    global winner
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        winner = True


def find_bomb():
    bomb_position = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                bomb_position.append(row)
                bomb_position.append(col)
    return bomb_position


def make_bombs(new_bomb_position):
    for i in range(0, len(new_bomb_position), 2):
        row, col = new_bomb_position[i], new_bomb_position[i + 1]
        for bomb_move in movement:
            new_row, new_col = row + movement[bomb_move][0], col + movement[bomb_move][1]
            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = "B"


def show_result(status="won"):
    [print(*matrix[row], sep="") for row in range(rows)]
    print(f"{status}: {player_row} {player_col}")
    exit()


player_row, player_col = find_player_position()
for command in commands:
    matrix[player_row][player_col] = "."
    player_movement_row, player_movement_col = player_row + movement[command][0], player_col + movement[command][1]
    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col
    make_bombs(find_bomb())
    if winner:
        show_result()
    if check_valid_index(player_movement_row, player_movement_col):
        player_alive(player_movement_row, player_movement_col)