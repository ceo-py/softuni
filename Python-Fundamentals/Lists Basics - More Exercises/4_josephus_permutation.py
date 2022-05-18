main_list = input().split(" ")
skip_number_k = int(input())
number_to_check = list()
final_numbers = list()

for number in main_list:
    number_to_check.append(int(number))

pos = skip_number_k - 1
index = 0
len_list = (len(number_to_check))

while len_list > 0:
    index = (pos + index) % len_list
    final_numbers.append(int(number_to_check.pop(index)))
    len_list -= 1


print(f"[{','.join(str(x) for x in final_numbers)}]")
