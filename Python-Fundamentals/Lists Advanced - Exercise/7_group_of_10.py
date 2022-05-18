number_list = [int(n) for n in input().split(", ")]

for n in range(1, 11):
    check_list = list()
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print(f"Group of {n * 10}'s: {check_list}")




# number_list = [int(n) for n in input().split(", ")]
#
# check_list = list()
# for n in range(1, 10 + 1):
#     check_list.clear()
#     if len(number_list) != 0:
#         for i in number_list:
#             if i <= (n * 10):
#                 check_list.append(i)
#         for o in check_list:
#             number_list.remove(o)
#
#         print(f"Group of {n * 10}'s: {check_list}")
