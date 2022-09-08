player_one, player_two = input().split(", ")

MATRIX_SIZE, game_info = 7, {player_one: {"Score": 501, "Turn": 0}, player_two: {"Score": 501, "Turn": 0},
                                         "D": 2, "T": 3}

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for row in range(MATRIX_SIZE)]


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def get_numbers(row, col , letter):
    total_sum = 0
    for r_num in (0, 6):
        total_sum += matrix[r_num][col]
    for c_col in (0, 6):
        total_sum += matrix[row][c_col]
    return total_sum * game_info[letter]


counter = 0
while game_info[player_one]["Score"] > 0 and game_info[player_two]["Score"] > 0:
    counter += 1

    if counter % 2 != 0:
        player = player_one
        game_info[player]["Turn"] += 1
    else:
        player = player_two
        game_info[player]["Turn"] += 1

    dart_row, dart_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
    if not check_valid_index(dart_row, dart_col):
        continue
    symbol = matrix[dart_row][dart_col]
    if isinstance(symbol, int):
        sum_to_extract = matrix[dart_row][dart_col]
    elif symbol in "DT":
        sum_to_extract = get_numbers(dart_row, dart_col, symbol)
    elif symbol == "B":
        sum_to_extract = game_info[player]["Score"]

    game_info[player]["Score"] -= sum_to_extract

print(f"{player} won the game with {game_info[player]['Turn']} throws!")




#
#
#
# MATRIX_SIZE = 7
#
# players = {x: 501 for x in input().split(", ")}
# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(MATRIX_SIZE)]
# player_one, player_two = list(players.keys())
# multiplys = {"D": 2, "T": 3}
#
#
# def check_valid_index(row, col):
#     return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE
#
#
# def multiply(row, col, letter, player):
#     total_sum = 0
#     for c_row in range(MATRIX_SIZE):
#         if str(matrix[c_row][col]).isdigit():
#             total_sum += matrix[c_row][col]
#     for c_col in range(MATRIX_SIZE):
#         if str(matrix[row][c_col]).isdigit():
#             total_sum += matrix[row][c_col]
#     players[player] -= total_sum * multiplys[letter]
#
#
# counter, turn = 0, 0
#
# while True:
#     counter += 1
#     hit_row, hit_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
#
#     if counter % 2 != 0:
#         turn += 1
#         player = player_one
#     else:
#         player = player_two
#
#     if check_valid_index(hit_row, hit_col):
#         symbol = matrix[hit_row][hit_col]
#         if str(symbol).isdigit():
#             players[player] -= symbol
#         elif symbol in "DT":
#             multiply(hit_row, hit_col, symbol, player)
#         elif symbol == "B":
#             print(f"{player} won the game with {turn} throws!")
#             break
#         if players[player] <= 0:
#             print(f"{player} won the game with {turn} throws!")
#             break




'''
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1'''