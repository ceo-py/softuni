class countdown_iterator:
    def __init__(self, counter):
        self.counter = counter

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == -1:
            raise StopIteration()

        output = self.counter
        self.counter -= 1
        return output

