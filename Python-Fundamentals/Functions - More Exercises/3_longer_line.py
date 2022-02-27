import math

x1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y1 = math.floor(float(input()))
y2 = math.floor(float(input()))
z1 = math.floor(float(input()))
z2 = math.floor(float(input()))
h1 = math.floor(float(input()))
h2 = math.floor(float(input()))

sum_x = math.floor(abs(x1) + abs(x2))
sum_y = math.floor(abs(y1) + abs(y2))
sum_z = math.floor(abs(z1) + abs(z2))
sum_h = math.floor(abs(h1) + abs(h2))
longer_line = list()

def whats_closer(arg1, arg2, arg3, arg4):
    longer_line.append(arg1)
    longer_line.append(arg2)
    longer_line.append(arg3)
    longer_line.append(arg4)
    longer_line.sort()
    # if longer_line[-2] == sum_x





print(whats_closer(sum_x, sum_y, sum_z, sum_h))
