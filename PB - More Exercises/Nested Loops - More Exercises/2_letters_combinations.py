import string


all_letters = string.ascii_lowercase

letter_a = input()
letter_b = input()
letter_c = input()

starting_point_loop = all_letters.index(letter_a)
ending_point_loop = all_letters.index(letter_b)
combinations = 0
for first_letter in all_letters[starting_point_loop:ending_point_loop+1]:
    for second_letter in all_letters[starting_point_loop:ending_point_loop+1]:
        for third_letter in all_letters[starting_point_loop:ending_point_loop+1]:
            if second_letter != letter_c != first_letter and third_letter != letter_c:
                combinations +=1
                print(f"{first_letter}{second_letter}{third_letter}", end=" ")
print(combinations)











#
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



#
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
