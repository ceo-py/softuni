import math

points = tuple(math.floor(float(input())) for _ in range(4))
sum_x = sum([abs(num) for num in points[:2]])
sum_y = sum([abs(num) for num in points[2:]])


def whats_closer(arg1, arg2):
    if arg1 <= arg2:
        return points[:2]
    return points[2:]


print(whats_closer(sum_x, sum_y))



#
#
#
#
#
#
#
# import math
#
# x1 = math.floor(float(input()))
# x2 = math.floor(float(input()))
# y1 = math.floor(float(input()))
# y2 = math.floor(float(input()))
#
# sum_x = math.floor(abs(x1) + abs(x2))
# sum_y = math.floor(abs(y1) + abs(y2))
#
#
# def whats_closer(arg1, arg2):
#     if arg1 <= arg2:
#         return f"({x1}, {x2})"
#
#     elif arg2 <= arg1:
#         return f"({y1}, {y2})"
#
#
# print(whats_closer(sum_x, sum_y))
