def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = f"<{tag}>{func(*args, *kwargs)}</{tag}>"
            return result

        return wrapper

    return decorator


@tags('g')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
