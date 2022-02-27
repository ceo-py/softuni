player_data = {}
while True:
    player = input()

    if player == "END":
        break

    goals = int(input())
    player_data[player] = goals

    if goals >= 10:
        break

player_data = sorted(player_data.items(), key=lambda x: x[1], reverse=True)

for name, goal in player_data:
    print(f"{name} is the best player!")

    if goal >= 3:
        print(f"He has scored {goal} goals and made a hat-trick !!!")

    else:

        print(f"He has scored {goal} goals.")
    break
