cozunak_numbers = int(input())

baker_best_name = ''
baker_best_score = 0


for cozunak_number in range(cozunak_numbers):

    baker_name = input()

    score = input()
    current_baker_score = 0
    while score != 'Stop':
        score = int(score)
        current_baker_score += score
        score = input()

    print(f'{baker_name} has {current_baker_score} points.')
    if current_baker_score > baker_best_score:
        baker_best_name = baker_name
        baker_best_score = current_baker_score
        print(f'{baker_best_name} is the new number 1!')


print(f'{baker_best_name} won competition with {baker_best_score} points!')








# easter_cake_number = int(input())
#
# to_stop = 100
# best_score = 0
# best_baker = ""
#
# for _ in range(0, easter_cake_number):
#     baker_name = input()
#     score = 0
#
#     for _ in range(0, to_stop):
#         score_number = input()
#
#         if score_number == "Stop":
#             if score > best_score:
#                 best_score = score
#                 best_baker = baker_name
#                 print(f"{baker_name} has {score} points.")
#                 print(f"{baker_name} is the new number 1!")
#                 break
#
#             else:
#                 print(f"{baker_name} has {score} points.")
#             break
#
#         else:
#             score += int(score_number)
#
# print(f"{best_baker} won competition with {best_score} points!")




# import sys
#
# breads = int(input())
# highest_points = -sys.maxsize
# best = ""
# for i in range(breads):
#     name_of_baker = input()
#     grade_per_person = input()
#     grade_per_baker = 0
#     while grade_per_person != 'Stop':
#         grade = int(grade_per_person)
#         grade_per_baker += grade
#         grade_per_person = input()
#
#     print(f"{name_of_baker} has {grade_per_baker} points.")
#     if grade_per_baker > highest_points:
#         highest_points = grade_per_baker
#         best = name_of_baker
#         print(f'{name_of_baker} is the new number 1!')
#
# print(f"{best} won competition with {highest_points} points!")
