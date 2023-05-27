from math import floor
tournament_count = int(input())
starting_points = int(input())
total_points = 0
percentage_wins = 0
for _ in range(tournament_count):
    finish = input()
    if finish == 'W':
        total_points += 2000
        percentage_wins += (len(finish) / tournament_count) * 100
    elif finish == 'F':
        total_points += 1200
    elif finish == 'SF':
        total_points += 720
final_points = total_points + starting_points
print(f'Final points: {final_points}')
print(f'Average points: {floor(total_points / tournament_count)}')
print(f"{percentage_wins:.2f}%")





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
#     total_points += + tournament_points[tournament_finish]
#     if tournament_finish == "W":
#         tournament_win_count += 1
#
# average_points = (total_points - starting_points) / tournaments_count
# tournament_win_percent = (tournament_win_count / tournaments_count) * 100
# print(f"Final points: {total_points}")
# print(f"Average points: {math.floor(average_points)}")
# print(f"{tournament_win_percent:.2f}%")

