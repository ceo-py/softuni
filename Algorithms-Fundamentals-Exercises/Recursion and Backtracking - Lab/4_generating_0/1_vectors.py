number = int(input())

result = [0] * number


def generate_vectors(idx, number):
    if idx >= len(result):
        print(*result, sep="")
        return
    for num in range(0, 2):
        result[idx] = num
        generate_vectors(idx + 1, number)


generate_vectors(0, number)
