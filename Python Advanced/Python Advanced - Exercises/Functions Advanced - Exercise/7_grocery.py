def grocery_store(**kwargs):
    result = ""
    for product_name, quantity in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result += f"{product_name}: {quantity}\n"
    return result

'''
quantity in descending order. If there are two or more products with the same quantity, 
sort them by their name's length in descending order. 
If there are two or more products with the same name's length, 
sort them by their name in ascending order (alphabetically). 
In the end, return a string in the following format:'''

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
