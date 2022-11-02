from itertools import permutations


def possible_permutations(numbers):
    output = permutations(numbers)

    for permutation in output:
        yield list(permutation)



