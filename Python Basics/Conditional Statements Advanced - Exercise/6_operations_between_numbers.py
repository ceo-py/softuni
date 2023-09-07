number_one = int(input())
number_two = int(input())
operator = input()


if number_one == 0 or number_two == 0:
    print(f'Cannot divide {number_one} by zero')

elif operator == '%':
    result = number_one % number_two
    print(f'{number_one} % {number_two} = {result}')

elif operator == '/':
    result = number_one / number_two
    print(f'{number_one} {operator} {number_two} = {result:.2f}')

else:
    result = eval(f'{number_one} {operator} {number_two}')

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'

    print(f'{number_one} {operator} {number_two} = {result} - {type_number}')



# number_one = int(input())
# number_two = int(input())
# operator = input()
#
# if number_one == 0 == number_two:
#     print(f"Cannot divide {number_one} by zero")
# elif operator == "/":
#     total = number_one / number_two
#     print(f"{number_one} / {number_two} = {total:.2f}")
# elif operator == "%":
#     total = number_one % number_two
#     print(f"{number_one} % {number_two} = {total}")
# else:
#     if operator == "+":
#         total = number_one + number_two
#     elif operator == "-":
#         total = number_one - number_two
#     elif operator == "*":
#         total = number_one * number_two
#     if total % 2 == 0:
#         print(f"{number_one} {operator} {number_two} = {total} - even")
#     else:
#         print(f"{number_one} {operator} {number_two} = {total} - odd")





#
#
# number_one = int(input())
# number_two = int(input())
# operator = input()
#
# if number_one == 0:
#      print(f"Cannot divide {number_one} by zero")
# elif number_two == 0:
#      print(f"Cannot divide {number_one} by zero")
# elif operator == "+":
#     total = number_one + number_two
#     if total % 2 == 0:
#         print(f"{number_one} + {number_two} = {total} - even")
#     else:
#         print(f"{number_one} + {number_two} = {total} - odd")
# elif operator == "-":
#     total = number_one - number_two
#     if total % 2 == 0:
#         print(f"{number_one} - {number_two} = {total} - even")
#     else:
#         print(f"{number_one} - {number_two} = {total} - odd")
# elif operator == "*":
#     total = number_one * number_two
#     if total % 2 == 0:
#         print(f"{number_one} * {number_two} = {total} - even")
#     else:
#         print(f"{number_one} * {number_two} = {total} - odd")
# elif operator == "/":
#     total = number_one / number_two
#     print(f"{number_one} / {number_two} = {total:.2f}")
# elif operator == "%":
#     total = number_one % number_two
#     print(f"{number_one} % {number_two} = {total}")
#




# num_1 = int(input())
# num_2 = int(input())
# operator = input()
#
# result = 0
#
# if num_1 == 0 or num_2 == 0:
#     print(f'Cannot divide {num_1} by zero')
# else:
#     if operator == '+':
#         result = num_1 + num_2
#     elif operator == '-':
#         result = num_1 - num_2
#     elif operator == '*':
#         result = num_1 * num_2
#     elif operator == '/':
#         result = num_1 / num_2
#     elif operator == '%':
#         result = num_1 % num_2
#     if operator == '+' or operator == '-' or operator == '*':
#         if result % 2 != 0:
#             print(f'{num_1} {operator} {num_2} = {result} - odd')
#         else:
#             print(f'{num_1} {operator} {num_2} = {result} - even')
#     elif operator == '/':
#             print(f"{num_1} / {num_2} = {result:.2f}")
#     elif operator == '%':
#             print(f"{num_1} % {num_2} = {result}")
#





# number_one = int(input())
# number_two = int(input())
# operator = input()
#
#
# def operator_action(number_one, number_two, operator):
#     if number_one == 0 == number_two:
#         return f"Cannot divide {number_one} by zero"
#     action = {"+": number_one + number_two,
#               "-": number_one - number_two,
#               "*": number_one * number_two,
#               "/": f"{(number_one / number_two):.2f}",
#               "%": number_one % number_two
#               }
#     if "%" != operator != "/":
#         if action[operator] % 2 == 0:
#             return f"{number_one} {operator} {number_two} = {action[operator]} - even"
#         else:
#             return f"{number_one} {operator} {number_two} = {action[operator]} - odd"
#     else:
#         return f"{number_one} {operator} {number_two} = {action[operator]}"
#
#
# print(operator_action(number_one, number_two, operator))