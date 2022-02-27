name_list = input().split(", ")
sorted_list = sorted(name_list, key= lambda x: (-len(x), x))
print(sorted_list)