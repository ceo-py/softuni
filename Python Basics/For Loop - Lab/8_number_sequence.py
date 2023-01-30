num = int(input())

max_number = float('-inf')
min_number = float('inf')
for i in range(num):
    number = int(input())
    if number >= max_number:
        max_number = number
    if number <= min_number:
        min_number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")



#
#
# input_number = int(input())
#
# numbers = list()
# for n in range(0, input_number):
#     numbers_to_sum = int(input())
#     numbers.append(numbers_to_sum)
#
# numbers.sort()
# print(f"Max number: {numbers[-1]}\nMin number: {numbers[0]}")
