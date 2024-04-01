shop_stock = {'sell_goods': 0}


def receive(quantity: int, food: str) -> None:
    if quantity <= 0:
        return
    shop_stock[food] = shop_stock.get(food, 0) + quantity


def sell(quantity: int, food: str) -> None:
    if food not in shop_stock:
        print(f'You do not have any {food}.')
        return

    if shop_stock[food] < quantity:
        shop_stock['sell_goods'] += shop_stock[food]
        print(
            f"There aren't enough {food}. You sold the last {shop_stock[food]} of them.")
    else:
        shop_stock['sell_goods'] += quantity
        print(f'You sold {quantity} {food}.')

    shop_stock[food] -= quantity
    if shop_stock[food] < 1:
        del shop_stock[food]


commands = {
    'Receive': receive,
    'Sell': sell,
}

command_input = input()

while command_input != 'Complete':
    command, *args = [int(x) if x.isdigit() else x for x in command_input.split(' ')]
    commands[command](*args)
    command_input = input()

[print(f'{k}: {v}') for k, v in list(shop_stock.items())[1:]]
print(f'All sold: {shop_stock["sell_goods"]} goods')
