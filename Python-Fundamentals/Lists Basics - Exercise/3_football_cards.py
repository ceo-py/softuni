team_information = input()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_list = team_information.split(" ")

for letter in team_list:

    if letter[0] == "A":
        if int(letter[2:]) in team_a:
            team_a.remove(int(letter[2:]))

    elif letter[0] == "B":
        if int(letter[2:]) in team_b:
            team_b.remove(int(letter[2:]))

    if len(team_a) < 7 or len(team_b) < 7:
        break

print(f"Team A - {len(team_a)}; Team B - {(len(team_b))}")

if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
