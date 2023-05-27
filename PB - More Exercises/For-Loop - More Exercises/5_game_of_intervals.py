number_of_moves = int(input())

result = 0

int_0_to_9 = 0
int_10_to_19 = 0
int_20_to_29 = 0
int_30_to_39 = 0
int_40_to_50 = 0
invalid_numbers = 0

for i in range(1, number_of_moves + 1):
    number = int(input())

    if number < 0 or number > 50:
        result /= 2
        invalid_numbers += 1
    elif 0 <= number <= 9:
        result += number * 0.20
        int_0_to_9 += 1
    elif 10 <= number <= 19:
        result += number * 0.30
        int_10_to_19 += 1
    elif 20 <= number <= 29:
        result += number * 0.40
        int_20_to_29 += 1
    elif 30 <= number <= 39:
        result += 50
        int_30_to_39 += 1
    elif 40 <= number <= 50:
        result += 100
        int_40_to_50 += 1

percent_numbers_0_to_9 = 100 * int_0_to_9 / number_of_moves
percent_numbers_10_to_19 = 100 * int_10_to_19 / number_of_moves
percent_numbers_20_to_29 = 100 * int_20_to_29 / number_of_moves
percent_numbers_30_to_39 = 100 * int_30_to_39 / number_of_moves
percent_numbers_40_to_50 = 100 * int_40_to_50 / number_of_moves
percent_invalid_numbers = 100 * invalid_numbers / number_of_moves

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_numbers_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_numbers_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_numbers_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_numbers_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_numbers_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")









# game_moves = int(input())
#
# total_score = 0
# from_zero_to_nine = 0
# from_ten_to_nineteen = 0
# from_twenty_to_twenty_nine = 0
# from_forty_to_fifty = 0
# from_thirty_to_thirty_nine = 0
# invalid_number = 0
#
# for _ in range(1, game_moves + 1):
#     number = int(input())
#
#     if 0 > number or number > 50:
#         invalid_number += 1
#         total_score = total_score / 2
#
#     elif number < 10:
#         from_zero_to_nine += 1
#         total_score += + (number * 0.20)
#
#     elif number < 20:
#         from_ten_to_nineteen += 1
#         total_score += + (number * 0.30)
#
#     elif number < 30:
#         from_twenty_to_twenty_nine += 1
#         total_score += + (number * 0.40)
#
#     elif number < 40:
#         from_thirty_to_thirty_nine += 1
#         total_score += + 50
#
#     elif number <= 50:
#         from_forty_to_fifty += 1
#         total_score += + 100
#
# from_zero_to_nine = (from_zero_to_nine / game_moves) * 100
# from_ten_to_nineteen = (from_ten_to_nineteen / game_moves) * 100
# from_twenty_to_twenty_nine = (from_twenty_to_twenty_nine / game_moves) * 100
# from_thirty_to_thirty_nine = (from_thirty_to_thirty_nine / game_moves) * 100
# from_forty_to_fifty = (from_forty_to_fifty / game_moves) * 100
# invalid_number = (invalid_number / game_moves) * 100
#
# print(f"{total_score:.2f}")
# print(f"From 0 to 9: {from_zero_to_nine:.2f}%")
# print(f"From 10 to 19: {from_ten_to_nineteen:.2f}%")
# print(f"From 20 to 29: {from_twenty_to_twenty_nine:.2f}%")
# print(f"From 30 to 39: {from_thirty_to_thirty_nine:.2f}%")
# print(f"From 40 to 50: {from_forty_to_fifty:.2f}%")
# print(f"Invalid numbers: {invalid_number:.2f}%")
