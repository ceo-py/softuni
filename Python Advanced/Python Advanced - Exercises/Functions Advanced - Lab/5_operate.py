def operate(operator, *args):
    result = args[0]
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for x in args[1:]:
            result -= x
    elif operator == "/":
        for x in args[1:]:
            result /= x
    elif operator == "*":
        for x in args[1:]:
            result *= x
    return result


# from functools import reduce
#
#
# def operate(operator, *args):
#     if operator == "+":
#         return reduce(lambda x, y: x + y, args)
#     elif operator == "-":
#         return reduce(lambda x, y: x - y, args)
#     elif operator == "*":
#         return reduce(lambda x, y: x * y, args)
#     elif operator == "/":
#         return reduce(lambda x, y: x / y, args)


'''((((1+2)+3)+4)+5)'''
# def operate(operator, *args):
#     return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)

'''x = 1
eval('x+1')
2'''
print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
