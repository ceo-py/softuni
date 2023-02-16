number_tournaments = int(input())
starting_points = int(input())

tournaments_points = 0
wins = 0

for tournament in range(number_tournaments):
    tournament_output = input()

    if tournament_output == "W":
        tournaments_points += 2000
        wins += 1

    elif tournament_output == "F":
        tournaments_points += 1200

    elif tournament_output == "SF":
        tournaments_points += 720

print(f"Final points: {starting_points + tournaments_points}")
print(f"Average points: {int(tournaments_points / number_tournaments)}")
print(f"{(wins / number_tournaments) * 100:.2f}%")












#
# import math
#
# tournaments_count = int(input())
# starting_points = int(input())
#
# tournament_points = {
#     "W": 2000,
#     "F": 1200,
#     "SF": 720
# }
# tournament_win_count = 0
# total_points = starting_points
#
# for torunament in range(0, tournaments_count):
#     tournament_finish = input()
#     total_points += tournament_points[tournament_finish]
#     if tournament_finish == "W":
#         tournament_win_count += 1
#
# average_points = (total_points - starting_points) / tournaments_count
# tournament_win_percent = (tournament_win_count / tournaments_count) * 100
# print(f"Final points: {total_points}")
# print(f"Average points: {math.floor(average_points)}")
# print(f"{tournament_win_percent:.2f}%")
