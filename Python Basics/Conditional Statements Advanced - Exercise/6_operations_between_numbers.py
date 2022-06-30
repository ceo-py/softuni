number_one = int(input())
number_two = int(input())
operator = input()

if number_one == 0 == number_two:
    print(f"Cannot divide {number_one} by zero")
elif operator == "/":
    total = number_one / number_two
    print(f"{number_one} / {number_two} = {total:.2f}")
elif operator == "%":
    total = number_one % number_two
    print(f"{number_one} % {number_two} = {total}")
else:
    if operator == "+":
        total = number_one + number_two
    elif operator == "-":
        total = number_one - number_two
    elif operator == "*":
        total = number_one * number_two
    if total % 2 == 0:
        print(f"{number_one} {operator} {number_two} = {total} - even")
    else:
        print(f"{number_one} {operator} {number_two} = {total} - odd")




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