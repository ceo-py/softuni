numbers_to_enter = int(input())

total_sum = 0
max_number = 0

for number in range(numbers_to_enter):

    input_number = int(input())

    if input_number > max_number:
        max_number = input_number

    total_sum += input_number

difference = total_sum - max_number

if difference == max_number:
    print('Yes')
    print(f'Sum = {max_number}')

else:
    print('No')
    print(f'Diff = {abs(difference - max_number)}')




# numbers_to_enter = int(input())
#
# numbers_input = list()
#
# for i in range(numbers_to_enter):
#     numbers_input.append(int(input()))
#
# numbers_input.sort()
# sum_of_all_numbers = sum(numbers_input) - numbers_input[-1]
# difrenc_numbers = numbers_input[-1] - (sum(numbers_input) - numbers_input[-1])
# if numbers_input[-1] == sum_of_all_numbers:
#     print(f"Yes\nSum = {numbers_input[-1]}")
# else:
#     print(f"No\nDiff = {abs(difrenc_numbers)}")






#
# n = int(input())
# list_numb = []
#
# for i in range(n):
#     numb = int(input())
#     list_numb.append(numb)
#
# if max(list_numb) == sum(list_numb) - max(list_numb):
#     print("Yes")
#     print(f"Sum = {max(list_numb)}")
# elif max(list_numb) != sum(list_numb) - max(list_numb):
#     difference = abs(max(list_numb) - (sum(list_numb) - max(list_numb)))
#     print("No")
#     print(f"Diff = {difference}")
#
#
