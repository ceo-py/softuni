numbers = [int(x) for x in input().split()]

result = sorted(x for x in numbers if x > sum(numbers)/len(numbers))

if result:
    print(*result[-5:][-1::-1])
else:
    print("No")



'''
564 47 -1 654 2 7
'''