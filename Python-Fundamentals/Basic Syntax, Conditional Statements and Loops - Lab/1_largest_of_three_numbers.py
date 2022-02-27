max_number = 0

for _ in range(3):
    number = int(input())

    if number > max_number or _ == 0:
        max_number = number

print(max_number)
