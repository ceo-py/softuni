name_of_the_football_team = input()
games_played_this_season = int(input())

w_games_count = 0
d_games_count = 0
l_games_count = 0
total_points = 0
win_rate = 0

if games_played_this_season == 0:
    print(f"{name_of_the_football_team} hasn't played any games during this season.")

else:
    for _ in range(0, games_played_this_season):
        game_result = input()

        if game_result == "W":
            w_games_count += 1
            total_points += 3

        elif game_result == "D":
            d_games_count += 1
            total_points += 1

        elif game_result == "L":
            l_games_count += 1
            total_points += 0

    win_rate = (w_games_count / games_played_this_season) * 100
    print(f"{name_of_the_football_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_games_count}")
    print(f"## D: {d_games_count}")
    print(f"## L: {l_games_count}")
    print(f"Win rate: {win_rate:.2f}%")
