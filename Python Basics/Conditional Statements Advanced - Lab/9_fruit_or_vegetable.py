product_name = input()

check_product = {
    "banana": "fruit",
    "apple": "fruit",
    "kiwi": "fruit",
    "cherry": "fruit",
    "lemon": "fruit",
    "grapes": "fruit",
    "tomato": "vegetable",
    "cucumber": "vegetable",
    "pepper": "vegetable",
    "carrot": "vegetable"
}

if product_name in check_product:
    print(check_product[product_name])
else:
    print("unknown")
