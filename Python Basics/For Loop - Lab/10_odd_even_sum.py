number_of_lines = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, number_of_lines + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:

    print('Yes')
    print(f'Sum = {even_sum}')

else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')










# number_enter = int(input())
#
# even_number = 0
# odd_number = 0
# count = 2
#
# for position in range(number_enter):
#     number = int(input())
#     if (position % 2) != 0:
#         odd_number += number
#     else:
#         even_number += number
#     count += 1
#
# if even_number == odd_number:
#     print(f"Yes\nSum = {abs(even_number)}")
# else:
#     total = odd_number - even_number
#     print(f"No\nDiff = {abs(total)}")







#
# iteration_count = int(input())
# sum_odd_nums = 0
# sum_even_nums = 0
# for i in range(1, iteration_count + 1):
#     number = int(input())
#     if i % 2 == 0:
#         sum_even_nums += number
#     else:
#         sum_odd_nums += number
# if sum_even_nums == sum_odd_nums:
#     print('Yes')
#     print(f'Sum = {sum_even_nums}')
# else:
#     difference = abs(sum_even_nums - sum_odd_nums)
#     print('No')
#     print(f'Diff = {difference}')
#
#
#







#
#
#
#
#
#
# number_enter = int(input())
#
# numbers = list()
# even_number = 0
# odd_number = 0
# count = 2
#
# for _ in range(number_enter):
#     number = int(input())
#     numbers.append(number)
# for number_one in numbers:
#     if (count % 2) != 0:
#         odd_number += number_one
#     else:
#         even_number += number_one
#     count += 1
#
# if even_number == odd_number:
#     print(f"Yes\nSum = {abs(even_number)}")
# else:
#     total = odd_number - even_number
#     print(f"No\nDiff = {abs(total)}")
