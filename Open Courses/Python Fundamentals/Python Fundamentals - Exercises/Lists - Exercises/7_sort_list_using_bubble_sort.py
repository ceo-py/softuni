def bubblesort(elements):
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]


elements = [int(x) for x in input().split()]

bubblesort(elements)
print(*elements)
