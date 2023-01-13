pin_one = int(input())
pin_two = int(input())
pin_three = int(input())

for num_one in range(1, pin_one + 1):
    for num_two in range(1, pin_two + 1):
        for num_three in range(1, pin_three + 1):
            if num_one % 2 == 0 and num_three % 2 == 0 and str(num_two) in "2357":
                print(f"{num_one} {num_two} {num_three}")