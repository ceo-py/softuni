list_one = input().split(", ")
list_two = input().split(", ")

result_list = list()

for n in list_one:
    for i in list_two:
        if n in i:
            result_list.append(n)
result_list = list(dict.fromkeys(result_list))
print(result_list)
