input_number = int(input())

numbers = list()
for n in range(0, input_number):
    numbers_to_sum = int(input())
    numbers.append(numbers_to_sum)

numbers.sort()
print(f"Max number: {numbers[-1]}\nMin number: {numbers[0]}")
