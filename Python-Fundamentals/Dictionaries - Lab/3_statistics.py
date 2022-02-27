product_input = input()
food_info_dic = dict()
while product_input != "statistics":
    food_type = product_input.split(": ")
    if food_type[0] not in food_info_dic:
        food_info_dic[food_type[0]] = 0
    food_info_dic[food_type[0]] = food_info_dic[food_type[0]] + int(food_type[-1])
    product_input = input()


def showing_products(dictionary):
    print("Products in stock:")
    total_products = 0
    total_quantity = 0
    for key, value in dictionary.items():
        print(f"- {key}: {value}")
        total_products += 1
        total_quantity += value
    print(f"Total Products: {total_products}")
    print(f"Total Quantity: {total_quantity}")


showing_products(food_info_dic)
