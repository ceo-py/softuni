tournament_days = int(input())

total_wins, total_money = 0, 0


for day in range(tournament_days):
    current_day_wins, current_day_money = 0, 0

    while True:
        sport = input()
        if sport == "Finish":
            total_wins += current_day_wins
            if current_day_wins > 0:
                current_day_money *= 1.10
            total_money += current_day_money
            break
        game_output = input()

        if game_output == "win":
            current_day_wins += 1
            current_day_money += 20
        elif game_output == "lose":
            current_day_wins -= 1

if total_wins > 0:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")






#
#
#
#
#
#
# days_of_the_tournament = int(input())
#
# total_money_win = 0
# win_count = 0
# loses_count = 0
# finish_day = 0
# total_money_tournament = 0
# wins_daily = 0
# loses_daily = 0
#
# while True:
#
#     tournamet_type = input()
#
#     if tournamet_type == "Finish":
#         finish_day += 1
#
#         if finish_day == days_of_the_tournament:
#
#             if wins_daily > loses_daily:
#                 total_money_win = total_money_win + total_money_win * 0.10
#                 total_money_tournament += total_money_win
#
#             else:
#                 total_money_tournament += total_money_win
#
#             if win_count > loses_count:
#                 total_money_tournament = total_money_tournament + total_money_tournament * 0.20
#                 print(f"You won the tournament! Total raised money: {total_money_tournament:.2f}")
#                 break
#
#             else:
#
#                 print(f"You lost the tournament! Total raised money: {total_money_tournament:.2f}")
#                 break
#
#         elif win_count < loses_count and finish_day == days_of_the_tournament:
#             total_money_win += total_money_win
#             break
#
#         elif wins_daily > loses_daily and finish_day != days_of_the_tournament:
#             total_money_win = total_money_win + total_money_win * 0.10
#             total_money_tournament += total_money_win
#             total_money_win = 0
#             wins_daily = 0
#             loses_daily = 0
#             tournamet_type = input()
#             win_or_lose_tournament = input()
#
#         elif wins_daily < loses_daily and finish_day != days_of_the_tournament:
#             total_money_tournament += total_money_win
#             total_money_win = 0
#             wins_daily = 0
#             loses_daily = 0
#             tournamet_type = input()
#             win_or_lose_tournament = input()
#
#     else:
#         win_or_lose_tournament = input()
#
#     if "win" == win_or_lose_tournament:
#         win_count += 1
#         wins_daily += 1
#         total_money_win += + 20
#
#     else:
#         loses_count += 1
#         loses_daily += 1
