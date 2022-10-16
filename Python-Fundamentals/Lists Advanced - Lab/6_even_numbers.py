main_list = [int(n) for n in input().split(", ")]
even_list = list()

for n, index in enumerate(main_list):
    if index % 2 == 0:
        even_list.append(n)

print(even_list)




# print([p for p, i in enumerate([int(i) for i in input().split(', ')]) if i % 2 == 0])