n = int(input())
l = int(input())

start_symbol_three = ord('a')

for symbol_one in range(1, n):

    for symbol_two in range(1, n + 2):

        for symbol_three in range(start_symbol_three, start_symbol_three + l):

            for symbol_four in range(start_symbol_three, start_symbol_three + l):

                for symbol_five in range(1, n + 3):

                    if symbol_one < symbol_five <= n and symbol_five > symbol_two:
                        print(f"{symbol_one}{symbol_two}{chr(symbol_three)}{chr(symbol_four)}{symbol_five}", end=" ")








    # import string
#
# n = int(input())
# l = int(input())
#
# alphabet_string_low = string.ascii_lowercase
# alphabet_list_lower = list(alphabet_string_low)
# l_letters = alphabet_list_lower[:l]
#
# for n_one in range(1, n):
#
#     for n_num in range(1, n + 2):
#
#         for l in l_letters:
#
#             for l_num in l_letters:
#
#                 for check in range(1, n + 3):
#
#                     if n_one < check and check > n_num and check <= n:
#                         print(f"{n_one}{n_num}{l}{l_num}{check}", end=" ")
