days_of_the_tournament = int(input())

total_money_win = 0
win_count = 0
loses_count = 0
finish_day = 0
total_money_tournament = 0
wins_daily = 0
loses_daily = 0

while True:

    tournamet_type = input()

    if tournamet_type == "Finish":
        finish_day += 1

        if finish_day == days_of_the_tournament:

            if wins_daily > loses_daily:
                total_money_win = total_money_win + total_money_win * 0.10
                total_money_tournament += total_money_win

            else:
                total_money_tournament += total_money_win

            if win_count > loses_count:
                total_money_tournament = total_money_tournament + total_money_tournament * 0.20
                print(f"You won the tournament! Total raised money: {total_money_tournament:.2f}")
                break

            else:

                print(f"You lost the tournament! Total raised money: {total_money_tournament:.2f}")
                break

        elif win_count < loses_count and finish_day == days_of_the_tournament:
            total_money_win += total_money_win
            break

        elif wins_daily > loses_daily and finish_day != days_of_the_tournament:
            total_money_win = total_money_win + total_money_win * 0.10
            total_money_tournament += total_money_win
            total_money_win = 0
            wins_daily = 0
            loses_daily = 0
            tournamet_type = input()
            win_or_lose_tournament = input()

        elif wins_daily < loses_daily and finish_day != days_of_the_tournament:
            total_money_tournament += total_money_win
            total_money_win = 0
            wins_daily = 0
            loses_daily = 0
            tournamet_type = input()
            win_or_lose_tournament = input()

    else:
        win_or_lose_tournament = input()

    if "win" == win_or_lose_tournament:
        win_count += 1
        wins_daily += 1
        total_money_win += + 20

    else:
        loses_count += 1
        loses_daily += 1
