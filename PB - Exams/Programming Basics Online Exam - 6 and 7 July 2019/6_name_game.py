player_name = input()

best_player_name = ''
best_player_score = 0

while player_name != 'Stop':

    current_player_score = 0

    for letter in player_name:
        current_score = int(input())

        if ord(letter) == current_score:
            current_player_score += 10

        else:
            current_player_score += 2

    if current_player_score >= best_player_score:
        best_player_score = current_player_score
        best_player_name = player_name

    player_name = input()

print(f'The winner is {best_player_name} with {best_player_score} points!')





# max_points = 0
# winner = ''
# name = input()
# while name != "Stop":
#     points = 0
#     for letter in name:
#         number = int(input())
#         if number == ord(letter):
#             points += 10
#         else:
#             points += 2
#     if points >= max_points:
#         winner = name
#         max_points = points
#     name = input()
# print(f'The winner is {winner} with {max_points} points!')



#
#
# total_points = 0
# first_name = ""
# second_name = ""
# total_points_for_name = 0
#
# while True:
#     name_of_the_player = input()
#     first_name = name_of_the_player
#     if name_of_the_player == "Stop":
#         print(f"The winner is {second_name} with {total_points} points!")
#         break
#
#     else:
#         for letter in name_of_the_player:
#             guesses_number = int(input())
#
#             if guesses_number == ord(letter):
#                 total_points_for_name += 10
#
#             else:
#                 total_points_for_name += 2
#
#         if total_points_for_name >= total_points:
#             total_points = total_points_for_name
#             second_name = name_of_the_player
#
#         total_points_for_name = 0



# total_points = 0
# first_name = ""
# second_name = ""
# total_points_for_name = 0
#
# while True:
#     name_of_the_player = input()
#     first_name = name_of_the_player
#     if name_of_the_player == "Stop":
#         print(f"The winner is {second_name} with {total_points} points!")
#         break
#
#     else:
#         for letter in name_of_the_player:
#             guesses_number = int(input())
#
#             if guesses_number == ord(letter):
#                 total_points_for_name += 10
#
#             else:
#                 total_points_for_name += 2
#
#         if total_points_for_name >= total_points:
#             total_points = total_points_for_name
#             second_name = name_of_the_player
#
#         total_points_for_name = 0



# stop = False
# b = []
# i = 0
# summ = 0
# winner_name = ''
# winner_score = 0
# while stop is False:
#     name = input()
#     b = list(name)
#     le = len(name)
#     if name == 'Stop':
#         stop = True
#         break
#     while le > 0:
#         n = input()
#         if n == 'Stop':
#             stop = True
#             break
#
#         if int(n) == ord(b[i]):
#                 summ += 10
#         elif int(n) != ord(b[i]):
#                 summ += 2
#         i += 1
#         le -= 1
#         if le == 0:
#             i = 0
#             break
#     if summ >= winner_score:
#         winner_name = name
#         winner_score = summ
#     summ = 0
#     if stop:
#         break
# print(f'The winner is {winner_name} with {winner_score} points!')
#
