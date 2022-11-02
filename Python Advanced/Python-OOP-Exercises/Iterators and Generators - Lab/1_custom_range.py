class custom_range:
    def __init__(self, start, end):
        self.end = end
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            output = self.start
            self.start += 1
            return output
        raise StopIteration()


# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)