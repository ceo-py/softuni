points = 0
wins = 0
loses = 0

while True:

    name_of_the_team = input()

    if name_of_the_team == "End of tournaments":
        total = wins + loses
        wins = wins / total * 100
        loses = loses / total * 100
        print(f"{wins:.2f}% matches win")
        print(f"{loses:.2f}% matches lost")
        break

    else:
        games_played = int(input())

        for game in range(1, games_played + 1):
            result_one = int(input())
            result_two = int(input())
            points = abs(result_one - result_two)

            if result_one > result_two:
                print(f"Game {game} of tournament {name_of_the_team}: win with {points} points.")
                points = 0
                wins += 1

            else:
                print(f"Game {game} of tournament {name_of_the_team}: lost with {points} points.")
                points = 0
                loses += 1
