from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"you called {func.__name__}{args}\nit returned {func(*args, **kwargs)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
