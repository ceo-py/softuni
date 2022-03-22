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


###
# n = int(input())
#
# for numbers in range(1111, 10000):
#     magic_number_find = True
#     for number in str(numbers):
#         if any(["0" in str(numbers), n % int(number) != 0]):
#             magic_number_find = False
#             break
#     if magic_number_find:
#         print(numbers, end=" ")

###

# n = int(input())
#
# for numbers in range(1111, 10000):
#     numbers = str(numbers)
#     if "0" not in numbers:
#         if all([n % int(numbers[0]) == 0, n % int(numbers[1]) == 0, n % int(numbers[2]) == 0,
#                 n % int(numbers[3]) == 0]):
#             print(numbers, end=" ")