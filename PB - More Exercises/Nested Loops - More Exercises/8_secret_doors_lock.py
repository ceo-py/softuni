number_one = int(input())
number_two = int(input())
number_three = int(input())

prime_numbers = [2, 3, 5, 7]

for hundreds in range(1, number_one + 1):

    for tens in range(1, number_two + 1):

        for units in range(1, number_three + 1):

            if hundreds % 2 == 0 and units % 2 == 0 and tens in prime_numbers:
                print(f"{hundreds} {tens} {units}")
