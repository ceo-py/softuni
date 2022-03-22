product = input()
quantity_of_the_product = int(input())

product_info = {
    "coffee": 1.50,
    "coke": 1.40,
    "water": 1.00,
    "snacks": 2.00
}


def calc_the_price(product_type, how_many):
    result = product_info[product_type] * how_many
    return f"{result:.2f}"


print(calc_the_price(product, quantity_of_the_product))
