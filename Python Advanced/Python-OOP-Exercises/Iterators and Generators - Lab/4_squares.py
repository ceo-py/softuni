def squares(param):
    num = 1

    while num <= param:
        yield num * num
        num += 1


