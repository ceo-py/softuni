main_list = input().lower().split()

result_dic = {float(x):main_list.count(x) for x in main_list}
[print(f"{key} -> {value} times") for key, value in sorted(result_dic.items(), key=lambda x: x[0])]




#
# main_list = input().lower().split()
#
# result_dic = {}
# for n in main_list:
#     result_dic[float(n)] = main_list.count(n)
#
# for key, value in sorted(result_dic.items(), key=lambda x: x[0]):
#     print(f"{key} -> {value} times")
