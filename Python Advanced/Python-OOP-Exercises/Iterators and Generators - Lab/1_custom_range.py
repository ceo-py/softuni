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

