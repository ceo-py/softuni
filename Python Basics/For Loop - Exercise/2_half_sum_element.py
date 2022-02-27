numbers_to_enter = int(input())

numbers_input = list()

for i in range(numbers_to_enter):
    numbers_input.append(int(input()))

numbers_input.sort()
sum_of_all_numbers = sum(numbers_input) - numbers_input[-1]
difrenc_numbers = numbers_input[-1] - (sum(numbers_input) - numbers_input[-1])
if numbers_input[-1] == sum_of_all_numbers:
    print(f"Yes\nSum = {numbers_input[-1]}")
else:
    print(f"No\nDiff = {abs(difrenc_numbers)}")
