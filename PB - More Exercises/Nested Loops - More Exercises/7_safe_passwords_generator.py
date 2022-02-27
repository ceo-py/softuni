import string

number_one = int(input())
number_two = int(input())
max_generated_passwords = int(input())


a_symbols = list(range(35, 56))
b_symbols = list(range(64, 97))


alphabet_string_upper = string.ascii_uppercase
numbers_generation = string.digits
alphabet_list_up = list(numbers_generation[1:] + alphabet_string_upper)
x = alphabet_list_up.index(number_one)
x_number = alphabet_list_up[:x + 1]

y = alphabet_list_up.index(number_one)
y_number = alphabet_list_up[:y + 1]