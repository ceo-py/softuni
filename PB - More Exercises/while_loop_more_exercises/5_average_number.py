total_numbers = int(input())

sum_of_numbers = 0

for i in range(0, total_numbers):
    number = int(input())
    sum_of_numbers += number

devided_numbers = sum_of_numbers / total_numbers
print(f"{devided_numbers:.2f}")