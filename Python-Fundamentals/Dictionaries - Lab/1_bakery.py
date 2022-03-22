food_type = input().split()

food_info_dic = dict()
i = 0
for string in food_type:
    if i % 2 == 0:
        food_info_dic[string] = 0
        name = string
    if i % 2 != 0:
        food_info_dic[name] = int(string)
        name = ""
    i += 1


# for i in range(0, len(food_type), 2):
#     food_info_dic[food_type[i]] = int(food_type[(i + 1)])


print(food_info_dic)
