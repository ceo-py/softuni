main_list = input().split()
result = [str(i) for i in sorted([int(i) for i in main_list])]
print(" <= ".join(result))