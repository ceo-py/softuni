items_accessories = input().split("|")
budget = int(input())

items_price, selling_items = list(), list()
budget_left = budget
train_ticket = 150

for clean_text in items_accessories:
    type_item, price = clean_text.split("->")
    price = float(price)
    if budget_left >= price:
        if any(["Clothes" in type_item and price <= 50, "Shoes" in type_item and price <= 35,
                "Accessories" in type_item and price <= 20.50]):
            items_price.append(price)
            budget_left -= price
            selling_items.append(price * 1.40)

difference = sum(selling_items) - sum(items_price)
for n in selling_items:
    print(f"{n:.2f}", end=" ")

print(f"\nProfit: {difference:.2f}")
if budget + difference > train_ticket:
    print(f"Hello, France!")
else:
    print("Not enough money.")


# items_accessories = input().split("|")
# budget = int(input())
#
# items_price = list()
# budget_left = budget
# selling_items = list()
# train_ticket = 150
#
# for clean_text in items_accessories:
#     if "Clothes->" in clean_text:
#         text = float(clean_text.replace("Clothes->", ""))
#
#         if 0 < text <= 50 and budget_left >= text:
#             items_price.append(text)
#             budget_left -= text
#             selling_items.append(text + text * 0.40)
#
#     elif "Shoes->" in clean_text:
#         text = float(clean_text.replace("Shoes->", ""))
#
#         if 0 < text <= 35 and budget_left >= text:
#             items_price.append(text)
#             budget_left -= text
#             selling_items.append(text + text * 0.40)
#
#     elif "Accessories->" in clean_text:
#         text = float(clean_text.replace("Accessories->", ""))
#
#         if 0 < text < 20.50 and budget_left >= text:
#             items_price.append(text)
#             budget_left -= text
#             selling_items.append(text + text * 0.40)
#
# for n in selling_items:
#     print(f"{n:.2f}", end=" ")
#
# normal_price = sum(items_price)
# re_sale = sum(selling_items)
# difference = re_sale - normal_price
#
# print(f"\nProfit: {difference:.2f}")
#
# if budget + difference > train_ticket:
#     print(f"Hello, France!")
# else:
#     print("Not enough money.")