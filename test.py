collection_of_items = input().split("|")
budget = int(input())
budget_left = budget
train_ticket = 150
total_money = 0
items_bought = []


def add_money(current_price):
    global total_money, budget_left
    total_money += current_price
    budget_left -= current_price


for index in collection_of_items:
    current_item, current_price = [float(x) if x[-1].isdigit() else x for x in index.split('->')]
    if budget_left >= current_price:
        if current_item == 'Clothes' and current_price <= 50:
            add_money(current_price)
            items_bought.append(current_price + (current_price * 0.40))
        elif current_item == 'Shoes' and current_price <= 35:
            add_money(current_price)
            items_bought.append(current_price + (current_price * 0.40))
        elif current_item == 'Accessories' and current_price <= 20.50:
            add_money(current_price)
            items_bought.append(current_price + (current_price * 0.40))

difference = sum(items_bought) - total_money
print(' '.join(f"{n:.2f}" for n in items_bought))
print(f'Profit: {difference:.2f}')
if budget + difference > train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')


