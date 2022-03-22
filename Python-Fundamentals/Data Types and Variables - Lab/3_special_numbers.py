number_input = int(input())
counter = 1
for number in range(1, number_input + 1):

    if counter >= 11:
        number = str(number)
        number_one = int(number[0])
        number_two = int(number[1])
        total = number_one + number_two

        if total == 11 or total == 5 or total == 7:
            print(f"{number} -> True")
            continue

    if number == 5 or number == 7:
        print(f"{number} -> True")

    else:
        print(f"{number} -> False")
    counter += 1


