budget = float(input())

is_budget_bigger = True
left_budget = budget
products_bought = 0
total_bought_products = 0
product_count = 0

while is_budget_bigger:

    product_name = input()
    product_count += 1
    if product_name == "Stop":
        print(f"You bought {products_bought} products for {total_bought_products:.2f} leva.")
        is_budget_bigger = False

    else:
        product_price = float(input())
        if product_count % 3 == 0:
            left_budget += - (product_price / 2)
            product_price = product_price / 2

        else:
            left_budget += - product_price

    if left_budget >= 0:
        products_bought += 1
        total_bought_products += product_price

    else:
        print(f"You don't have enough money!\nYou need {abs(left_budget):.2f} leva!")
        is_budget_bigger = False
