from functools import wraps


def even_parameters(func):
    def is_even_number(n):
        return n % 2 == 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        for el in args:
            if isinstance(el, str) or not is_even_number(el):
                return "Please use only even numbers!"
        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
