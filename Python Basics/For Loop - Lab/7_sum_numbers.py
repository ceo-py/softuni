enter_number = int(input())
numbers = list()
total = 0
for n in range(0, enter_number):
    numbers_to_sum = int(input())
    numbers.append(numbers_to_sum)

for _ in numbers:
    total += _
print(total)