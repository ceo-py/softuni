a = int(input())
b = int(input())
max_count = int(input())
counter = 0

for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                counter += 1

                if counter > max_count:
                    exit()
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                if x == a and y == b:
                    exit()
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64






#
#
#
#
#
#
# import string
#
# number_one = int(input())
# number_two = int(input())
# max_generated_passwords = int(input())
#
#
# a_symbols = list(range(35, 56))
# b_symbols = list(range(64, 97))
#
#
# alphabet_string_upper = string.ascii_uppercase
# numbers_generation = string.digits
# alphabet_list_up = list(numbers_generation[1:] + alphabet_string_upper)
# x = alphabet_list_up.index(number_one)
# x_number = alphabet_list_up[:x + 1]
#
# y = alphabet_list_up.index(number_one)
# y_number = alphabet_list_up[:y + 1]
