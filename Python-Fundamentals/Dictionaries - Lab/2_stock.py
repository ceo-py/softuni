initial_list = input().split()
food_type = {initial_list[i]: int(initial_list[i + 1]) for i in range(0, len(initial_list), 2)}

searching_for_food = input().split()
for product in searching_for_food:
    if product in food_type:
        print(f'We have {food_type[product]} of {product} left')
        continue

    print(f"Sorry, we don't have {product}")




# food_type = input().split()
# searching_for_food = input().split()
# food_info_dic = dict()
# i = 0
# for string in food_type:
#     if i % 2 == 0:
#         food_info_dic[string] = 0
#         name = string
#     if i % 2 != 0:
#         food_info_dic[name] = int(string)
#         name = ""
#     i += 1
#
# for product in searching_for_food:
#     if product in food_info_dic:
#         print(f"We have {food_info_dic[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")