class custom_range:
    def __init__(self, start, end, step=None):
        self.start = start
        self.end = end
        self.step = step
        self.counter = 0
        self.incrementator = 1

        if step and step < 0:
            self.start, self.end = self.end, self.start
            self.incrementator = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.incrementator < 0:
            if self.start >= self.end:
                temp = self.start
                self.start += self.incrementator
                return temp
        else:
            if self.start <= self.end:
                temp = self.start
                self.start += self.incrementator
                return temp
        raise StopIteration()