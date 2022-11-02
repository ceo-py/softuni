class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ('a', 'e', 'i', 'o', 'u')

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                letter, self.string = self.string[0], self.string[1:]
                if letter.lower() in self.vowels:
                    return letter
            except IndexError:
                raise StopIteration()





