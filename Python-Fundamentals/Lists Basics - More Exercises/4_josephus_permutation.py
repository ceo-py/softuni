main_list = input().split()
skip_number_k = int(input())

final_numbers = list()
pos = skip_number_k - 1
index = 0
len_list = (len(main_list))

while len_list > 0:
    index = (pos + index) % len_list
    final_numbers.append(main_list.pop(index))
    len_list -= 1


print(f"[{','.join(final_numbers)}]")









#
# from collections import deque
#
#
# person = deque(input().split())
# execute_num = int(input())
# result = []
#
# while len(person) > 1:
#     person.rotate(-execute_num)
#     result.append(person.pop())
#
# result.append(person.pop())
# print(f"[{','.join(result)}]")
#
#
#
