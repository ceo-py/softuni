starting_point = int(input())
ending_point = int(input())
looking_number = int(input())

count_combinations = 0
combination_found = 0

for number_one in range(starting_point, ending_point + 1):

    if combination_found == 1:
        break

    for number_two in range(starting_point, ending_point + 1):
        count_combinations += 1

        if number_one + number_two == looking_number:
            total = number_one + number_two
            print(f"Combination N:{count_combinations} ({number_one} + {number_two} = {total})")
            combination_found = 1
            break

if combination_found == 0:
    print(f"{count_combinations} combinations - neither equals {looking_number}")
