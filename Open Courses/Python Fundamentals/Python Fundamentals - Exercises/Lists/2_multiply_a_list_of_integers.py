numbers = input().split()
multiply = int(input())


def show_result(n, m):
    return f"{' '.join([str(x) for x in [int(num) * m for num in n]])}"


print(show_result(numbers, multiply))




# numbers = input().split()
# multiply = int(input())
#
#
# def show_result(n, m):
#     result = []
#     for num in n:
#         result.append(int(num) * m)
#     print(*result)
#
#
# show_result(numbers, multiply)
