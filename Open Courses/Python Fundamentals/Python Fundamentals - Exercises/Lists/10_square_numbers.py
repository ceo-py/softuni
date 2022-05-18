import math

main_list = sorted([int(x) for x in input().split() if math.sqrt(abs(int(x))).is_integer() and int(x) > 0], reverse=True)


print(*main_list)



# import math
#
# main_list = [int(x) for x in input().split() if math.sqrt(abs(int(x))).is_integer() and int(x) > 0]
# main_list.sort(reverse=True)
#
# print(*main_list)