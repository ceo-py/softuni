max_points = 0
winner = ''
name = input()
while name != "Stop":
    points = 0
    for letter in name:
        number = int(input())
        if number == ord(letter):
            points += 10
        else:
            points += 2
    if points >= max_points:
        winner = name
        max_points = points
    name = input()
print(f'The winner is {winner} with {max_points} points!')



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
