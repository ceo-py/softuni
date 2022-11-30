from functools import wraps


def even_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        nums = func(*args, **kwargs)
        return [num for num in nums if num % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5, 8]))
