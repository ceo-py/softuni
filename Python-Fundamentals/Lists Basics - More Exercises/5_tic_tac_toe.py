first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

first_player_win = None

if len(set(first_line)) == 1 and first_line[0] == "1":
    first_player_win = True

elif len(set(second_line)) == 1 and second_line[0] == "1":
    first_player_win = True

elif len(set(third_line)) == 1 and third_line[0] == "1":
    first_player_win = True


elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "1":
    first_player_win = True

elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "1":
    first_player_win = True

elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "1":
    first_player_win = True

elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "1":
    first_player_win = True

elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "1":
    first_player_win = True

elif len(set(first_line)) == 1 and first_line[0] == "2":
    first_player_win = False

elif len(set(second_line)) == 1 and second_line[0] == "2":
    first_player_win = False

elif len(set(third_line)) == 1 and third_line[0] == "2":
    first_player_win = False

elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "2":
    first_player_win = False

elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "2":
    first_player_win = False

elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "2":
    first_player_win = False

elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "2":
    first_player_win = False

elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "2":
    first_player_win = False


if first_player_win is None:
    print("Draw!")

elif first_player_win:
    print("First player won")

else:
    print("Second player won")
