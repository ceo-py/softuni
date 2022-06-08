elements_count = int(input())

elements = []
for _ in range(elements_count):
    for element in input().split():
        elements.append(element)

print("\n".join(set(elements)))