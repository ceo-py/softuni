def fibonacci():
    last_num = 0
    current_num = 1

    yield last_num
    yield current_num

    while True:
        next_num = last_num + current_num
        yield next_num
        last_num, current_num = current_num, next_num


