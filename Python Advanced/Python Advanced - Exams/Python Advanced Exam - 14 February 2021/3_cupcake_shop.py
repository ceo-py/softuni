def stock_availability(*args):
    inventory = [x for x in args[0]]
    parameters = args[1:]
    if parameters[-1] == "sell":
        inventory = inventory[1:]
    elif isinstance(parameters[-1], int):
        inventory = inventory[parameters[-1]:]
    else:
        for item in args[2:]:
            if parameters[0] == "delivery":
                inventory.append(item)
            elif item in inventory:
                while item in inventory:
                    inventory.remove(item)

    return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
