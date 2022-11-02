class reverse_iter:
    def __init__(self, list_of_numbers: list):
        self.list_of_numbers = list_of_numbers
        self.index = len(list_of_numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            output = self.list_of_numbers[self.index]
            self.index -= 1
            return output
        else:
            raise StopIteration()




# class reverse_iter:
#     def __init__(self, list_of_numbers: list):
#         self.list_of_numbers = list_of_numbers[::-1]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return self.list_of_numbers.pop()
#         except IndexError:
#             raise StopIteration()
