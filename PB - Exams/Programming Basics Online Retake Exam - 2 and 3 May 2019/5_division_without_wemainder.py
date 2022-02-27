full_numbers = int(input())

divide_two = 0
divide_three = 0
divide_four = 0

for _ in range(0, full_numbers):
    number = int(input())
    if number % 2 == 0:
        divide_two += 1

    if number % 3 == 0:
        divide_three += 1

    if number % 4 == 0:
        divide_four += 1

divide_two = (divide_two / full_numbers) * 100
divide_three = (divide_three / full_numbers) * 100
divide_four = (divide_four / full_numbers) * 100
print(f"{divide_two:.2f}%")
print(f"{divide_three:.2f}%")
print(f"{divide_four:.2f}%")


