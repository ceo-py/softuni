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

i = 1
print("[", end="")
len_list = (len(main_list))
for n in final_numbers:
    if i != len_list:
        print(f"{n},", end="")
    else:
        print(f"{n}]")
    i += 1
