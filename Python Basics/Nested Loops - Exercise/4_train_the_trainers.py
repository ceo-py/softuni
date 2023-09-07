judges_count = int(input())

presentation_name = input()
total_score = 0
total_presentations = 0

while presentation_name != 'Finish':
    total_presentations += judges_count
    current_score = 0

    for score in range(judges_count):
        current_score += float(input())

    total_score += current_score
    print(f'{presentation_name} - {current_score / judges_count:.2f}.')

    presentation_name = input()

print(f"Student's final assessment is {total_score / total_presentations:.2f}.")







# judges_count = int(input())
#
# presentations_info = {}
# counter = 0
# total_average_score = 0
# score_numbers = 0
# while True:
#     presentation_name = input()
#     if presentation_name == "Finish":
#         break
#     presentations_info[presentation_name] = 0
#     for judge in range(judges_count):
#         score = float(input())
#         presentations_info[presentation_name] += score
#         counter += 1
#         total_average_score += score
#         score_numbers += 1
#     presentations_info[presentation_name] = presentations_info[presentation_name] / counter
#     counter = 0
#
# total_average_score = total_average_score / score_numbers
# for key, value in presentations_info.items():
#     print(f"{key} - {value:.2f}.")
# print(f"Student's final assessment is {total_average_score:.2f}.")
