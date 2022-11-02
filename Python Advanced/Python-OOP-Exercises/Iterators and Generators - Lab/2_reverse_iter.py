class reverse_iter:
    def __init__(self, list_of_numbers: list):
        self.list_of_numbers = list_of_numbers

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return self.list_of_numbers.pop()
            except IndexError:
                raise StopIteration()
