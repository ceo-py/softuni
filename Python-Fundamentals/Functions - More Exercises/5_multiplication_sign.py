number_one = int(input())
number_two = int(input())
number_three = int(input())


def check_numbers(*input_list):
    if any(x == 0 for x in input_list):
        return "zero"

    if sum(x < 0 for x in input_list) % 2 != 0:
        return "negative"

    return "positive"


print(check_numbers(number_one, number_two, number_three))





# number_one = int(input())
# number_two = int(input())
# number_three = int(input())
#
#
# def check_numbers(one, two, three):
#     if (three > 0 and one < 0 and two < 0) or \
#             (two > 0 and one < 0 and three < 0) or \
#             (one > 0 and two < 0 and three < 0) or \
#             (one > 0 and two > 0 and three > 0):
#         return "positive"
#     elif one == 0 or two == 0 or three == 0:
#         return "zero"
#
#     elif one < 0 or two < 0 or three < 0:
#         return "negative"
#
#
# print(check_numbers(number_one, number_two, number_three))