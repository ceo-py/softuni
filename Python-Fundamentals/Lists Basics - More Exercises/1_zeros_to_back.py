numbers = list(map(int, input().strip().split(", ")))

for _ in numbers:
    numbers.append(numbers.pop(numbers.index(0)))
print(numbers)
