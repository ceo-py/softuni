numbers_range = int(input())


for _ in range(numbers_range):
    num = int(input())
    if 2 % num == 0:
        print(f"{num} is odd!")
        break
else:
    print("All numbers are even.")
