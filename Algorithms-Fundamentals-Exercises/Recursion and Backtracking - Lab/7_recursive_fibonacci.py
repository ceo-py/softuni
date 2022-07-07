n = int(input())


def fib_of(n):
    if n <= 1:
        return 1
    return fib_of(n - 1) + fib_of(n - 2)


print(fib_of(n))




#
# n = int(input())
#
#
# def loop_fib(num):
#     fib0 = 1
#     fib1 = 1
#     result = 0
#     for _ in range(num - 1):
#         result = fib0 + fib1
#         fib0, fib1 = fib1, fib0
#     return result
#
#
# print(loop_fib(n))

#
# number = int(input())
# FibArray = [0, 1]
#
#
# def fibonacci_of(n):
#     if n in {0, 1}:
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)
#
#
# print(sum([fibonacci_of(n) for n in range(number)]) + 1)
#
#
