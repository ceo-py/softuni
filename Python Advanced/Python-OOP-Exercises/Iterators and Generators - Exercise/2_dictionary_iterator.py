class dictionary_iter:

    def __init__(self, dict_: dict):
        self.items = list(dict_.items())
        self.iters = len(dict_)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.iters:
            raise StopIteration()
        output = self.items[self.start]
        self.start += 1
        return output

