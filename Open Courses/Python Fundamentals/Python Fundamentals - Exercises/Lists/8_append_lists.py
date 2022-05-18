main_list = input()

result_list = []
last_result = []
total = ""
for pos, num in enumerate(main_list):
    if num == "|":
        result_list.append(total.split())
        total = ""
    else:
        total += num
result_list.append(total.split())
for n in result_list:
    last_result.insert(0, n)

for n in last_result:
    for i in n:
        print(i, end=" ")
