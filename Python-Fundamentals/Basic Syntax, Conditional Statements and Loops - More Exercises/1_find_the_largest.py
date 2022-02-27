number_input = input()

numbers = list(number_input)
numbers.sort(reverse=True)

for i in numbers:
    print(i, end="")
