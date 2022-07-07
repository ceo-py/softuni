from collections import deque

list_with_numbers = deque(int(x) for x in input().split())


def recursive_sum(list_with_numbers):
    if len(list_with_numbers) == 1:
        return list_with_numbers[0]
    return list_with_numbers.popleft() + recursive_sum(list_with_numbers)


print(recursive_sum(list_with_numbers))




#
# list_with_numbers = [int(x) for x in input().split()]
#
#
# def calc_sum(numbers, idx):
#     if idx == len(numbers) - 1:
#         return  numbers[idx]
#     return numbers[idx] + calc_sum(numbers, idx + 1)
#
#
# print(calc_sum(list_with_numbers, 0))






