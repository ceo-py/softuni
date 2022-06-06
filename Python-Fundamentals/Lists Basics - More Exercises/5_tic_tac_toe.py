game_matrix = []
winner = {
    0: "Draw!",
    1: "First player won",
    2: "Second player won",
    "player": 0
}

for _ in range(3):
    game_matrix.append([int(num) for num in input().split()])
# horizontal check
for line in game_matrix:
    if len(set(line)) == 1:
        winner["player"] = line[0]
        break
else:  # vertical check
    test_diagonals = [[], []]
    for col in range(3):
        test_diagonals[0].append(game_matrix[col][col])
        test_diagonals[1].append(game_matrix[col][::-1][col])
        for player in range(1, 3):
            if all([game_matrix[0][col] == game_matrix[1][col] == game_matrix[2][col] == player]):
                winner["player"] = game_matrix[0][col]
                break
    else:
         # diagonal check
        for diagonal in test_diagonals:
            if len(set(diagonal)) == 1:
                winner["player"] = diagonal[0]
                break

print(winner[winner["player"]])














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
