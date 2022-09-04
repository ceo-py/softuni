dictionary = {'name': 'Peter', 'age': 25}


def kwargs_length(**kwargs):
    return len(kwargs)


print(kwargs_length(**dictionary))