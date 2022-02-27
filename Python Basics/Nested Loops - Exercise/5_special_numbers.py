number_to_check = int(input())



for number_one in range(1, 9):
    if number_to_check % number_one == 0:

        for number_two in range(1, 9):
            if number_to_check % number_two == 0:

                for number_three in range(1, 9):
                    if number_to_check % number_three == 0:

                        for number_four in range(1, 9):
                            if number_to_check % number_four == 0:
                                print(f"{number_one}{number_two}{number_three}{number_four}", end=" ")