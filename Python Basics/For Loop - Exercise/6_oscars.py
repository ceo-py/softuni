actor_name = input()
points_from_academy = float(input())
judges_number = int(input())

judges_score = points_from_academy


for judge in range(0, judges_number):
    judge_name = input()
    judge_points = float(input())

    judges_score += (len(judge_name) * (judge_points / 2))

    if judges_score > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {judges_score:.1f}!")
        break

else:
    judges_score = 1250.5 - judges_score
    print(f"Sorry, {actor_name} you need {judges_score:.1f} more!")




# name = input()
# score = float(input())
# comiss = int(input())
# if 2.0 <= score <= 450.5 and 1 <= comiss <= 20:
#     while comiss > 0:
#         if score <= 1250.5:
#             com_name = input()
#             com_name_score = float(input())
#             if 1.0 <= com_name_score <= 50.0:
#                 points = len(com_name)*com_name_score/2
#                 score = score + points
#             else:
#                 pass
#         comiss -= 1
#     if score > 1250.5:
#         print(f'Congratulations, {name} got a nominee for leading role with {score:.1f}!')
#     else:
#         print(f'Sorry, {name} you need {(1250.5 - score):.1f} more!')
#
#