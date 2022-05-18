number_elements = int(input())
elements = [int(x) for x in input().split()]
# even = []
# odd = []
result = []
i = 0
add_element= ""
if number_elements % 2 != 0:
    add_element = elements[-1]
    i = 1
else:
    i = 2


for pos in range(1, number_elements // 2 + i):
    if pos % 2 == 0:
        if elements[pos] >= elements[pos + 1]:
            result.append(elements[pos])
            result.append(elements[pos + 1])
        else:
            result.append(elements[pos + 1])
            result.append(elements[pos])


    else:
        if elements[pos - 1] >= elements[pos]:
            result.append(elements[pos - 1])
            result.append(elements[pos])
        else:
            result.append(elements[pos])
            result.append(elements[pos - 1])


# sorting_hope = sorted(elements, key = lambda )


if add_element:
    result.append(add_element)
    print(*result, sep=" ")

# for pos, x in enumerate(elements, 1):
#     if pos % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
#
# for i, (e, o) in enumerate(zip(even, odd)):
#     if o >= e <= odd[i+2]:
#         result.append(o)
#         result.append(e)
#     else:
#         result.append(e)
#         result.append(o)
# if number_elements % 2 != 0:
#     result.append(odd[-1])
#
# print(*result, sep=" ")
