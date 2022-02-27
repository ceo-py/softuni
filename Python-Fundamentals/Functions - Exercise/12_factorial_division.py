import math

number_one = int(input())
number_two = int(input())


def factorial_division(one, two):
    one = math.factorial(one)
    two = math.factorial(two)
    return f"{(one / two):.2f}"


print(factorial_division(number_one, number_two))
