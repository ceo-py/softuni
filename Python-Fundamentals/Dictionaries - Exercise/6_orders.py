command = input()

drinks_info = {}
price_d = "price"
quantity_d = "quantity"

while command != "buy":
    name, price, quantity = [float(x) if x[-1].isdigit() else x for x in command.split()]
    drinks_info[name] = drinks_info.get(name, {})
    drinks_info[name][price_d] = drinks_info[name].get(price_d, 0)
    drinks_info[name][quantity_d] = drinks_info[name].get(quantity_d, 0)
    drinks_info[name][price_d] = price
    drinks_info[name][quantity_d] += quantity
    command = input()

for product_name in drinks_info:
    result = drinks_info[product_name][price_d] * drinks_info[product_name][quantity_d]
    print(f"{product_name} -> {result:.2f}")






#
# command = input()
#
# drinks_info = {}
# while command != "buy":
#     command = command.split()
#     name = command[0]
#     price = float(command[1])
#     quantity = int(command[-1])
#     quantity_left = 0
#     if name not in drinks_info:
#         drinks_info[name] = {}
#         drinks_info[name][price] = 0
#     else:
#         quantity_left = list(drinks_info[name].values())
#         quantity_left = quantity_left[0]
#         drinks_info[name].clear()
#         drinks_info[name] = {}
#         drinks_info[name][price] = 0
#
#     drinks_info[name][price] += quantity + quantity_left
#     command = input()
#
# for i in drinks_info:
#     for key, value in drinks_info[i].items():
#         result = key * value
#         print(f"{i} -> {result:.2f}")
#
#
#
