main_list = input().lower().split()

result_dic = {n: main_list.count(n) for n in main_list if main_list.count(n) % 2 != 0}
print(*result_dic.keys(), sep=", ")




# main_list = input().lower().split()
#
# result_dic = {}
# for n in main_list:
#     num = main_list.count(n)
#     if num % 2 != 0:
#         result_dic[n] = num
#
# print(*result_dic.keys(), sep=", ")
