product_name = input()

output = 'unknown'

if product_name in 'banana, apple, kiwi, cherry, lemon, grapes':
    output = 'fruit'

elif product_name in 'tomato, cucumber, pepper, carrot':
    output = 'vegetable'


print(output)




# product_name = input()
#
# check_product = {
#     "banana": "fruit",
#     "apple": "fruit",
#     "kiwi": "fruit",
#     "cherry": "fruit",
#     "lemon": "fruit",
#     "grapes": "fruit",
#     "tomato": "vegetable",
#     "cucumber": "vegetable",
#     "pepper": "vegetable",
#     "carrot": "vegetable"
# }
#
# print(check_product.get(product_name, 'unknown'))

