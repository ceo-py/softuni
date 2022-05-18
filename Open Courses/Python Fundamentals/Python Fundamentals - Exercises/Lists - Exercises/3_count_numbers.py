main_list = [int(x) for x in input().split()]
showed_number = {x:main_list.count(x) for x in sorted(main_list)}
[print(f"{n} -> {i}") for n, i in showed_number.items()]





# main_list = [int(x) for x in input().split()]
# showed_number = []
# for num in sorted(main_list):
#     if num not in showed_number:
#         print(f"{num} -> {main_list.count(num)}")
#         showed_number.append(num)