class take_skip:
    def __init__(self, step: int, range_: int):
        self.range_ = range_
        self.step = step
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.range_:
            raise StopIteration()
        output = self.iterations * self.step
        self.iterations += 1
        return output



# class take_skip:
#     def __init__(self, step: int, range_: int):
#         self.range_ = range_
#         self.step = step
#         self.current_num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.range_ > 0:
#             self.range_ -= 1
#             output = self.current_num
#             self.current_num += self.step
#             return output
#         else:
#             raise StopIteration()