numbers_range = int(input())


for _ in range(numbers_range):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        break
else:
    print("All numbers are even.")