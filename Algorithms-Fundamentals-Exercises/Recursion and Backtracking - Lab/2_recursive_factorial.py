number = int(input())


def recursive_factorial(number):
    if number == 1:
        return number
    return number * recursive_factorial(number - 1)


print(recursive_factorial(number))




# number = int(input())
#
# score = 1
# for n in range(1, number + 1):
#     score *= n
#
# print(score)