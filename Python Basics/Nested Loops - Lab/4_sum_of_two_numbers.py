number = int(input())
number_end = int(input())
magic_number = int(input())

combinations_count = 0
stop = 0

for x1 in range(number, number_end + 1):
    for x2 in range(number, number_end + 1):
        if x1 + x2 == magic_number:
            combinations_count += 1
            total = x1 + x2
            stop += 1
            print(f"Combination N:{combinations_count} ({x1} + {x2} = {total})")
            break
        else:
            combinations_count += 1
    if x1 + x2 == magic_number:
        total = x1 + x2
        stop += 1
        break

if stop != 2:
    print(f"{combinations_count} combinations - neither equals {magic_number}")







# n_begin = int(input())
# n_end = int(input())
# magic = int(input())
# coun = 0
# found_combo = False
# for i in range(n_begin, n_end + 1):
#     for j in range(n_begin, n_end + 1):
#         coun += 1
#         if i + j == magic:
#             found_combo = True
#             break
#     if found_combo:
#         break
#
# if found_combo:
#     print(f'Combination N:{coun} ({i} + {j} = {magic})')
# else:
#     print(f'{coun} combinations - neither equals {magic}')
#