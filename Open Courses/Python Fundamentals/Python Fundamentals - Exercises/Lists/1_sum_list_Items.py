number_range = int(input())


def sum_numbers(n):
    return sum([int(input()) for _ in range(n)])


print(sum_numbers(number_range))




# number_range = int(input())
#
#
# def sum_numbers(n):
#     total_ = []
#     for _ in range(n):
#         total_.append(int(input()))
#     return sum(total_)
#
#
# print(sum_numbers(number_range))
