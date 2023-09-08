start_letter = input()
end_letter = input()
skip_letter = input()


letter_ascii_number = ord(skip_letter)
start_loop_range = ord(start_letter)
end_loop_range = ord(end_letter) + 1
found_combinations = 0

for first_letter in range(start_loop_range, end_loop_range):
    for middle_letter in range(start_loop_range, end_loop_range):
        for end_letter in range(start_loop_range, end_loop_range):

            if first_letter != letter_ascii_number and middle_letter != letter_ascii_number and end_letter != letter_ascii_number:
                found_combinations += 1
                print(f'{chr(first_letter)}{chr(middle_letter)}{chr(end_letter)}', end=' ')

print(found_combinations)




# import string
#
# all_letters = string.ascii_lowercase
#
# letter_a = input()
# letter_b = input()
# letter_c = input()
#
# starting_point_loop = all_letters.index(letter_a)
# ending_point_loop = all_letters.index(letter_b)
# combinations_of_letters = all_letters[starting_point_loop:ending_point_loop + 1]
# combinations_of_letters = combinations_of_letters.replace(letter_c, "")
# combinations = 0
# for first_letter in combinations_of_letters:
#     for second_letter in combinations_of_letters:
#         for third_letter in combinations_of_letters:
#             combinations += 1
#             print(f"{first_letter}{second_letter}{third_letter}", end=" ")
# print(combinations)





# import itertools
#
# first_letter = input()
# second_letter = input()
# skip_letter = input()
#
# lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#            'w', 'x', 'y', 'z']
#
# index_letter_one = lower_a.index(first_letter)
# index_letter_two = lower_a.index(second_letter)
# checking_letters = lower_a[index_letter_one:index_letter_two + 1]
# if skip_letter in checking_letters:
#     index_skip_letter = checking_letters.index(skip_letter)
#     del checking_letters[index_skip_letter]
# combinations_count = 0
#
# for r in range(3, 4):
#     for s in itertools.product(checking_letters, repeat=r):
#         print(''.join(s), end=" ")
#         combinations_count += 1
#
# print(combinations_count)






# import string
#
# all_letters = string.ascii_lowercase
#
# letter_a = input()
# letter_b = input()
# letter_c = input()
#
# starting_point_loop = all_letters.index(letter_a)
# ending_point_loop = all_letters.index(letter_b)
# skip_letter = all_letters.index(letter_c)
# combinations = 0
# for pos, first_letter in enumerate(all_letters[starting_point_loop:ending_point_loop + 1], starting_point_loop):
#     if pos != skip_letter:
#         for pos, second_letter in enumerate(all_letters[starting_point_loop:ending_point_loop + 1],
#                                             starting_point_loop):
#             if pos != skip_letter:
#                 for pos, third_letter in enumerate(all_letters[starting_point_loop:ending_point_loop + 1],
#                                                    starting_point_loop):
#                     if pos != skip_letter:
#                         combinations += 1
#                         print(f"{first_letter}{second_letter}{third_letter}", end=" ")
# print(combinations)

