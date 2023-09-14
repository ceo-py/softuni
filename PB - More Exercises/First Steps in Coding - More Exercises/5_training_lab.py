import math

length = float(input())
width = float(input())

corridor = 100
desk_width = 70
desk_length = 120
width = math.floor(((width * 100) - corridor) / desk_width)
length = math.floor(((length * 100) / desk_length))
other_space = 3

total_space = width * length - other_space
print(total_space)







#
# w = float(input())
# h = float(input())
#
# chair_h = 70
# chair_w = 120
#
# total_w = w * 100
# total_h = h * 100
#
# free_row_h = total_h - 100
# chair_row_h = free_row_h // chair_h
#
#
# chair_row_w = total_w // chair_w
#
# all_chairs = int((chair_row_h * chair_row_w) - 3)
#
# print(all_chairs)
