first_row = input().split()
second_row = input().split()
third_row = input().split()

name_player = "First"
found = False

for player in range(1, 3):
    player = str(player)
    line = [player, player, player]
    if line == first_row or second_row == line or third_row == line:  # преверка на редовете
        found = True
    for index in range(0, 3):
        if first_row[index] == player and second_row[index] == player and third_row[index] == player:  # проверка на колоните
            found = True
    if first_row[0] == player and second_row[1] == player and third_row[2] == player:  # ляв диагонал
        found = True
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player:  # десен диагонал
        found = True
    if found:
        print(f"{name_player} player won")
        break
    name_player = "Second"
else:
    print("Draw!")



# first_row = input().split()
# second_row = input().split()
# third_row = input().split()
#
# winner = {
#     "1": "First",
#     "2": "Second"
# }
#
#
# def tic_tac(player):
#     lines = [player] * 3
#     if any([lines == first_row, second_row == lines, third_row == lines]):
#         return player
#     for row in range(0, 3):
#         if all([first_row[row] == player, second_row[row] == player, third_row[row] == player]):
#             return player
#     if all([first_row[0] == player, second_row[1] == player, third_row[2] == player]):
#         return player
#     elif all([first_row[2] == player, second_row[1] == player, third_row[0] == player]):
#         return player
#
#
# for player in range(1, 3):
#     player_win = tic_tac(str(player))
#     if any([player_win == "1", player_win == "2"]):
#         print(f"{winner[player_win]} player won")
#         break
# else:
#     print("Draw!")








#
# game_matrix = []
# winner = {
#     0: "Draw!",
#     1: "First player won",
#     2: "Second player won",
#     "player": 0
# }
#
# for _ in range(3):
#     game_matrix.append([int(num) for num in input().split()])
# # horizontal check
# for line in game_matrix:
#     if len(set(line)) == 1:
#         winner["player"] = line[0]
#         break
# else:  # vertical check
#     test_diagonals = [[], []]
#     for col in range(3):
#         test_diagonals[0].append(game_matrix[col][col])
#         test_diagonals[1].append(game_matrix[col][::-1][col])
#         for player in range(1, 3):
#             if all([game_matrix[0][col] == game_matrix[1][col] == game_matrix[2][col] == player]):
#                 winner["player"] = game_matrix[0][col]
#                 break
#     else:
#          # diagonal check
#         for diagonal in test_diagonals:
#             if len(set(diagonal)) == 1:
#                 winner["player"] = diagonal[0]
#                 break
#
# print(winner[winner["player"]])
#
#




#
# field = []
#
# first_player_win = False
# second_player_win = False
# draw = False
# #  drawing the game field in separate lists
# for field_row in range(3):
#     current_row = input().split()
#     field.append(current_row)
# #  checking each row to see if there is a winner in the row
# for row in range(3):
#     if field[row][0] == field[row][1] == field[row][2] != "0":
#         if field[row][0] == field[row][1] == field[row][2] == "1":
#             first_player_win = True
#         elif field[row][0] == field[row][1] == field[row][2] == "2":
#             second_player_win = True
# #  checking each column to see if there is a winner in the column
# for col in range(3):
#     if field[0][col] == field[1][col] == field[2][col] != "0":
#         if field[0][col] == field[1][col] == field[2][col] == "1":
#             first_player_win = True
#         elif field[0][col] == field[1][col] == field[2][col] == "2":
#             second_player_win = True
# #  checking left diagonal if there is a winner
# if field[0][0] == field[1][1] == field[2][2] != "0":
#     if field[0][0] == field[1][1] == field[2][2] == "1":
#         first_player_win = True
#     elif field[0][0] == field[0][1] == field[2][2] == "2":
#         second_player_win = True
# #  checking right diagonal if there is a winner
# elif field[0][2] == field[1][1] == field[2][0] != "0":
#     if field[0][2] == field[1][1] == field[2][0] == "1":
#         first_player_win = True
#     elif field[0][2] == field[1][1] == field[2][0] == "2":
#         second_player_win = True
# # if there is no winner found the game is a draw
# if not first_player_win and not second_player_win:
#     draw = True
#
# if first_player_win:
#     print("First player won")
# elif second_player_win:
#     print("Second player won")
# elif draw:
#     print("Draw!")






#
#
#
# first_line = input().split(" ")
# second_line = input().split(" ")
# third_line = input().split(" ")
#
# first_player_win = None
#
# if len(set(first_line)) == 1 and first_line[0] == "1":
#     first_player_win = True
#
# elif len(set(second_line)) == 1 and second_line[0] == "1":
#     first_player_win = True
#
# elif len(set(third_line)) == 1 and third_line[0] == "1":
#     first_player_win = True
#
# elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "1":
#     first_player_win = True
#
# elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "1":
#     first_player_win = True
#
# elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "1":
#     first_player_win = True
#
# elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "1":
#     first_player_win = True
#
# elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "1":
#     first_player_win = True
#
# elif len(set(first_line)) == 1 and first_line[0] == "2":
#     first_player_win = False
#
# elif len(set(second_line)) == 1 and second_line[0] == "2":
#     first_player_win = False
#
# elif len(set(third_line)) == 1 and third_line[0] == "2":
#     first_player_win = False
#
# elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "2":
#     first_player_win = False
#
# elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "2":
#     first_player_win = False
#
# elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "2":
#     first_player_win = False
#
# elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "2":
#     first_player_win = False
#
# elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "2":
#     first_player_win = False
#
#
# if first_player_win is None:
#     print("Draw!")
#
# elif first_player_win:
#     print("First player won")
#
# else:
#     print("Second player won")
