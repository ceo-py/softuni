n = int(input())
left_sum = 0
right_sum = 0
for number in range(0, n*2):
    current_num = int(input())
    if number < n:
        left_sum+=current_num
    elif number >=n:
        right_sum+=current_num

if left_sum == right_sum:
    print('Yes, sum = ' + str(right_sum))
else:
    diff = abs(left_sum-right_sum)
    print('No, diff = '+ str(diff))