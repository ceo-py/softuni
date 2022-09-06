def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    product_in_card, output = 0, ""
    for product, (price, quantity) in kwargs.items():
        total_price = price * quantity
        if total_price <= budget:
            output += f"You bought {product} for {total_price:.2f} leva.\n"
            product_in_card += 1
            budget -= total_price
            if product_in_card == 5:
                break
    return output



# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))