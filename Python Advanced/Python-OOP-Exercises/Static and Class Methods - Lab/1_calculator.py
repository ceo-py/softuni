class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        output = 1
        for x in args:
            output *= x
        return output

    @staticmethod
    def divide(*args):
        output = args[0]
        for x in args[1:]:
            output /= x
        return output

    @staticmethod
    def subtract(*args):
        output = args[0]
        for x in args[1:]:
            output -= x
        return output



# from functools import reduce
#
#
# class Calculator:
#
#     @staticmethod
#     def add(*args):
#         return reduce(lambda x, y: x + y, args)
#
#     @staticmethod
#     def multiply(*args):
#         return reduce(lambda x, y: x * y, args)
#
#     @staticmethod
#     def divide(*args):
#         return reduce(lambda x, y: x / y, args)
#
#     @staticmethod
#     def subtract(*args):
#         return reduce(lambda x, y: x - y, args)