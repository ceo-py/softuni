def reverse_text(param):
    while param:
        yield param[-1]
        param = param[:-1]

