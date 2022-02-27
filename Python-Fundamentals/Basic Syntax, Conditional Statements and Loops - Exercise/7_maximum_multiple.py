number_divisor = int(input())
number_boundary = int(input())

target_number = 0
for number in range(1, number_boundary + 1):
    number_check = number / number_divisor
    if 0 < number <= number_boundary and number_check.is_integer():
        target_number = number

print(target_number)
