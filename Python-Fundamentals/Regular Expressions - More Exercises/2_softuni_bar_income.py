import re
total_income = 0
pattern = re.compile(
    r"(%)(?P<customer>[A-Z][a-z]+)\1([^\|\$\%\.]*)"
    r"<(?P<product>[\w]+)>([^\|\$\%\.]*)"
    r"\|(?P<count>[\d]+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$")


data_input = input()

while data_input != "end of shift":
    result = re.finditer(pattern, data_input)
    for show in result:
        current_price = float(show["count"]) * float(show["price"])
        print(f"{show['customer']}: {show['product']} - {current_price:.2f}")
        total_income += current_price
    data_input = input()

print(f"Total income: {total_income:.2f}")








#
#
# import re
#
# customers = input()
# customer_name, product_name, price_product, value_product = re.compile(r"\%{1}([A-Z]{1}[a-z]{1,})\%{1}"), \
#     re.compile(r"\<{1}([\w]{1,})\>{1}"),re.compile(r"\|{1}(\d{1,})\|{1}"),re.compile(r"(\d+\.\d+)\b([$]){1}|(\d+\d+)\b([$]){1}")
# total_income = 0
# while customers != "end of shift":
#
#     name_d, product_d, price_d, value_d = re.finditer(customer_name, customers), \
#                                         re.finditer(product_name, customers), re.finditer(price_product,
#                                         customers), re.finditer(    value_product, customers)
#
#     name_find = None
#     product_find = None
#     price_find = None
#     value_find = None
#     for show, p_name, p_price, p_value in zip(name_d, product_d, price_d, value_d):
#         name_find = show[1]
#         product_find = p_name[1]
#         price_find = float(p_price[1])
#         if p_value[1] is None:
#             value_find = float(p_value[3])
#         elif p_value[3] is None:
#             value_find = float(p_value[1])
#
#     if all([name_find is not None, product_find is not None,
#             price_find is not None, value_find is not None]):
#         print(f"{name_find}: {product_find} - {(price_find * value_find):.2f}")
#         total_income += (price_find * value_find)
#
#     customers = input()
#
# print(f"Total income: {total_income:.2f}")
