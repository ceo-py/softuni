def shopping_cart(*args):
    result, output = {"Dessert": [], "Pizza": [], "Soup": []}, []
    for info in args:
        if info == "Stop":
            break
        meal, product = info

        if product not in result[meal]:
            if meal == "Soup" and len(result[meal]) != 3:
                result[meal].append(product)
            elif meal == "Pizza" and len(result[meal]) != 4:
                result[meal].append(product)
            elif meal == "Dessert" and len(result[meal]) != 2:
                result[meal].append(product)

    for s_meal, s_product in sorted(result.items(), key= lambda x: (-len(x[1]), x[0])):
        output.append(f"{s_meal}:")
        for a_product in sorted(s_product):
            output.append(f" - {a_product}")

    if any(len(x) != 0 for x in result.values()):
        return '\n'.join(output)

    return "No products in the cart!"








# def shopping_cart(*args):
#     output, result = "", {"Dessert": [], "Pizza": [], "Soup": []}
#     for info in args:
#         if "Stop" in info:
#             break
#         meal, product, = info
#         for meal_type, number_product in (("Soup", 3), ("Pizza", 4), ("Dessert", 2)):
#             if meal == meal_type and len(result[meal]) != number_product and product not in result[meal]:
#                 result[meal].append(product)
#                 break
#     for p_meal, p_product in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
#         output += f"{p_meal}:\n"
#         for item in sorted(p_product):
#             output += f" - {item}\n"
#     if len(output) == 22:
#         output = "No products in the cart!"
#     return output
#
#


#
# def shopping_cart(*args):
#     output, result = "", {"Dessert": [], "Pizza": [], "Soup": []}
#     for info in args:
#         if "Stop" in info:
#             break
#         meal, product,  = info
#         if meal == "Soup" and len(result[meal]) != 3 and product not in result[meal]:
#             result[meal].append(product)
#         elif meal == "Pizza" and len(result[meal]) != 4 and product not in result[meal]:
#             result[meal].append(product)
#         elif meal == "Dessert" and len(result[meal]) != 2 and product not in result[meal]:
#             result[meal].append(product)
#     for p_meal, p_product in sorted(result.items(), key= lambda x: (-len(x[1]), x[0])):
#         output += f"{p_meal}:\n"
#         for item in sorted(p_product):
#             output += f" - {item}\n"
#     if len(output) == 22:
#         output = "No products in the cart!"
#     return output
#
#




'''
Pizza:
 - cheese
 - flour
 - ham
 - mushrooms
Dessert:
 - milk
Soup:
 - carrots
'''

'''
    n the end, sort the meals by the number of bought products in descending order. 
    If there are meals with an equal number of products, sort them (the meals) by their name 
    in ascending order (alphabetically). For each meal sort its products in ascending order (alphabetically).'''

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
