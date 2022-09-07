def numbers_searching(*args):
    return [sorted(set(range(min(args), max(args))) - set(args))[0], sorted(list(set([x for n, x in enumerate(args) if x in args[:n]])))]



#
#
# def numbers_searching(*args):
#     missing_numbers = sorted(set(range(min(args), max(args))) - set(args))[0]
#     duplicate_numbers = sorted(list(set([x for n, x in enumerate(args) if x in args[:n]])))
#     return [missing_numbers, duplicate_numbers]
#
#

print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

