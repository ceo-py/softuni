MATRIX_SIZE = 6

players = {x: {"rest": False} for x in input().split(", ")}
matrix = [input().split() for _ in range(MATRIX_SIZE)]


def find_exit(row, col, player):
    if matrix[row][col] == "E":
        print(f"{player[0]} found the Exit and wins the game!")
        exit()


def trap(row, col, player):
    if matrix[row][col] == "T":
        print(f"{player[0]} is out of the game! The winner is {player[1]}.")
        exit()


def wall(row, col, player):
    if matrix[row][col] == "W":
        players[player[0]]["rest"] = True
        print(f"{player[0]} hits a wall and needs to rest.")


commands = {"E": find_exit, "T": trap, "W": wall}


player_one, player_two = list(players.keys())
player_counter = 0


while True:
    input_row, input_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
    player_counter += 1
    if player_counter % 2 == 0:
        player = (player_two, player_one)
    else:
        player = (player_one, player_two)
    if players[player[0]]["rest"]:
        players[player[0]]["rest"] = False
        continue
    player_steps_on = matrix[input_row][input_col]
    if player_steps_on != ".":
        commands[player_steps_on](input_row, input_col, player)

'''
Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)'''