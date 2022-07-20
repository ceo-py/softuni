count = int(input())
previous_sum = int(input()) + int(input())
max_difference = 0

for i in range(count - 1):
    current_sum = int(input()) + int(input())
    max_difference = max(max_difference, abs(previous_sum - current_sum))
    previous_sum = current_sum

if max_difference == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")




#
#
# count = int(input())
# previous_sum = int(input()) + int(input())
# max_difference = 0
#
# for i in range(count - 1):
#     current_sum = int(input()) + int(input())
#     sum_abs = abs(previous_sum - current_sum)
#     if sum_abs > max_difference:
#         max_difference = sum_abs
#
#     previous_sum = current_sum
#
# if max_difference == 0:
#     print(f"Yes, value={previous_sum}")
# else:
#     print(f"No, maxdiff={max_difference}")
#
#



#
#
# n = int(input())
#
# curr_pair_sum = 0
# prev_pair_sum = 0
# max_diff_pair = 0
#
# for i in range(2 * n):
#     curr = int(input())
#     curr_pair_sum += curr
#
#     if i % 2 != 0 and i >= 3:
#         pairs = abs(curr_pair_sum - prev_pair_sum)
#         if max_diff_pair < pairs:
#             max_diff_pair = pairs
#         prev_pair_sum = curr_pair_sum
#         curr_pair_sum = 0
#
#     elif i % 2 != 0 and i >= 1:
#         prev_pair_sum = curr_pair_sum
#         curr_pair_sum = 0
#
# if max_diff_pair == 0:
#     print(f"Yes, value={prev_pair_sum}")
# else:
#     print(f"No, maxdiff={max_diff_pair}")
#
#
#
#




# n = int(input())
#
# curr_pair_sum = 0
# prev_pair_sum = 0
# max_diff_pair = 0
#
# for i in range(2 * n):
#     curr = int(input())
#     curr_pair_sum += curr
#
#     if i % 2 != 0 and i >= 3:
#         max_diff_pair = max(max_diff_pair, abs(curr_pair_sum - prev_pair_sum))
#         prev_pair_sum = curr_pair_sum
#         curr_pair_sum = 0
#
#     elif i % 2 != 0 and i >= 1:
#         prev_pair_sum = curr_pair_sum
#         curr_pair_sum = 0
#
# if max_diff_pair == 0:
#     print(f"Yes, value={prev_pair_sum}")
# else:
#     print(f"No, maxdiff={max_diff_pair}")





#
#
# total_numbers_to_check = int(input())
#
# equal_numbers = 0
# number_a = int(input())
# number_b = int(input())
# check_number_one = number_a + number_b
# all_numbers = list()
# all_numbers.append(check_number_one)
# total_check = list()
# i = 0
# diffrence = 0
#
# for _ in range(1, total_numbers_to_check):
#     number_a = int(input())
#     number_b = int(input())
#     check_number_two = number_a + number_b
#     all_numbers.append(check_number_two)
#
#     if check_number_one == check_number_two:
#         equal_numbers += 1
#         check_number_one = check_number_two
#
# how_long = len(all_numbers)
#
# if total_check == 2:
#     diffrence = check_number_one - check_number_two
#
# elif total_check == 1:
#     diffrence = number_a - number_b
#
# else:
#
#     for _ in range(1, how_long):
#         number_one = all_numbers[i]
#         number_two = all_numbers[i + 1]
#         i += 1
#         first_pair = abs(number_one - number_two)
#
#         if first_pair > diffrence:
#             diffrence = first_pair
#
# if equal_numbers >= 1 or total_numbers_to_check == 1:
#     print(f"Yes, value={check_number_one}")
#
# else:
#     print(f"No, maxdiff={abs(diffrence)}")
