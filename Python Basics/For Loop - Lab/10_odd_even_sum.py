number_enter = int(input())

even_number = 0
odd_number = 0
count = 2

for position in range(number_enter):
    number = int(input())
    if (position % 2) != 0:
        odd_number += number
    else:
        even_number += number
    count += 1

if even_number == odd_number:
    print(f"Yes\nSum = {abs(even_number)}")
else:
    total = odd_number - even_number
    print(f"No\nDiff = {abs(total)}")






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
