items_accessories = input().split("|")
budget = int(input())

items_price = list()
budget_left = budget
selling_items = list()
train_ticket = 150

for clean_text in items_accessories:
    if "Clothes->" in clean_text:
        text = clean_text.replace("Clothes->", "")

        if 0 < float(text) <= 50 and budget_left >= float(text):
            items_price.append(float(text))
            budget_left -= float(text)
            selling_items.append(float(text) + (float(text) * 0.40))

    elif "Shoes->" in clean_text:
        text = clean_text.replace("Shoes->", "")

        if 0 < float(text) <= 35 and budget_left >= float(text):
            items_price.append(float(text))
            budget_left -= float(text)
            selling_items.append(float(text) + (float(text) * 0.40))

    elif "Accessories->" in clean_text:
        text = clean_text.replace("Accessories->", "")

        if 0 < float(text) < 20.50 and budget_left >= float(text):
            items_price.append(float(text))
            budget_left -= float(text)
            selling_items.append(float(text) + (float(text) * 0.40))

for n in selling_items:
    print(f"{n:.2f}", end=" ")

normal_price = sum(items_price)
re_sale = sum(selling_items)
difference = re_sale - normal_price

print(f"\nProfit: {difference:.2f}")

if budget + difference > train_ticket:
    print(f"Hello, France!")
else:
    print("Not enough money.")
