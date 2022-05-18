main_list = [print(f"Index {pos} -> {num}") for pos, num in enumerate(input().split()) if all([abs(int(num)) % 2 != 0, pos % 2 != 0])]




# main_list = [int(x) for x in input().split()]
#
#
# def check_numbers():
#     for pos, num in enumerate(main_list):
#         if all([abs(num) % 2 != 0, pos % 2 != 0]):
#             print(f"Index {pos} -> {num}")
#
#
# check_numbers()




# main_list = [int(x) for x in input().split()]
#
# index_list = []
# numbers_ = []
#
#
# def check_numbers():
#     for pos, num in enumerate(main_list):
#         if abs(num) % 2 != 0 and pos % 2 != 0:
#             index_list.append(pos)
#             numbers_.append(num)
#     if index_list:
#         for pos, num in zip(index_list, numbers_):
#             print(f"Index {pos} -> {num}")
#
#
# check_numbers()
