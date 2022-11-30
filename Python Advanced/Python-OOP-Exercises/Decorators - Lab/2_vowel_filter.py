from functools import wraps


def vowel_filter(func):
    VOWELS = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [char for char in result if char in VOWELS]

    return wrapper


@vowel_filter
def get_letters(text):
    return text


print(get_letters(["a", "b", "c", "d", "e"]))
print(get_letters("GoGo"))
