first_game_result = input()
second_game_result = input()
third_game_result = input()

wins = 0
losses = 0
draw = 0

if int(first_game_result[0]) > int(first_game_result[2]):
    wins += 1

elif int(first_game_result[0]) == int(first_game_result[2]):
    draw += 1

else:
    losses += 1

if int(second_game_result[0]) > int(second_game_result[2]):
    wins += 1

elif int(second_game_result[0]) == int(second_game_result[2]):
    draw += 1

else:
    losses += 1

if int(third_game_result[0]) > int(third_game_result[2]):
    wins += 1

elif int(third_game_result[0]) == int(third_game_result[2]):
    draw += 1

else:
    losses += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draw}")
