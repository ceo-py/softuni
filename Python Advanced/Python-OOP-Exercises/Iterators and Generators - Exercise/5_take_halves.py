def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for x in integers():
            yield x / 2

    def take(n, num):
        return [next(num) for _ in range(n)]

    return take, halves, integers

