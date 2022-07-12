saved_money = 0

while True:
    destination = input()

    if destination == 'End':
        break

    minimum_money = float(input())
    saved_money = 0

    while saved_money < minimum_money:
        saved = float(input())
        saved_money += saved

    print(f'Going to {destination}!')



#
#
#
# destination = input()
# budget = float(input())
#
# destination_name = destination
# going_to_destination = list()
# destination_budget = budget
# destination_save = 0
# checking_for_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# while True:
#     infomation = input()
#     if infomation[0] in checking_for_numbers:
#         destination_save += float(infomation)
#     else:
#         if destination_save >= destination_budget:
#             going_to_destination.append(destination_name)
#         destination_budget = 0
#         destination_save = 0
#         destination_name = infomation
#         if infomation == "End":
#             for towns in going_to_destination:
#                 print(f"Going to {towns}!")
#             break
#         destination_budget = float(input())
