main_list = [x for x in input().split() if int(x) > 0]
if main_list:
    print(*main_list[::-1])
else:
    print("empty")
