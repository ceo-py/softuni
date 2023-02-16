game_one_result = input()
game_two_result = input()
game_three_result = input()


wins = 0
loses = 0
draws = 0

if int(game_one_result[0]) > int(game_one_result[-1]):
    wins += 1
elif int(game_one_result[0]) < int(game_one_result[-1]):
    loses += 1
else:
    draws += 1

if int(game_two_result[0]) > int(game_two_result[-1]):
    wins += 1
elif int(game_two_result[0]) < int(game_two_result[-1]):
    loses += 1
else:
    draws += 1

if int(game_three_result[0]) > int(game_three_result[-1]):
    wins += 1
elif int(game_three_result[0]) < int(game_three_result[-1]):
    loses += 1
else:
    draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")




# wins = 0
# loses = 0
# draws = 0
# 
# for games in range(3):
#     game_result = input()
#     if int(game_result[0]) > int(game_result[-1]):
#         wins += 1
#     elif int(game_result[0]) < int(game_result[-1]):
#         loses += 1
#     else:
#         draws += 1
# 
# print(f"Team won {wins} games.")
# print(f"Team lost {loses} games.")
# print(f"Drawn games: {draws}")