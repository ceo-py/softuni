text_test = input().split()

sum_number = 0
list_a = list()
list_b = list()
rest = list()
i = 0
result = 0
for text in text_test:
    for letter in text:
        if i == 0:
            list_a.append(ord(letter))
        else:
            list_b.append(ord(letter))
    i += 1

how_long_a = len(list_a)
how_long_b = len(list_b)
equal_list = False
diffrence = abs(how_long_a - how_long_b)
if how_long_a > how_long_b:
    for a, b in zip(list_a, list_b):
        result += a * b
    result += sum(list_a[-diffrence:])
elif how_long_b > how_long_a:
    for a, b in zip(list_a, list_b):
        result += a * b
    result += sum(list_b[-diffrence:])
elif how_long_b == how_long_a:
    for a, b in zip(list_a, list_b):
        result += a * b
        equal_list = True

if equal_list:
    print(result)
else:
    print(result)
