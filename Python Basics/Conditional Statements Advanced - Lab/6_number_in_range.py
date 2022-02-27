number = int(input())

if number == 0:
    print("No")
elif number in range(-100, 101):
    print("Yes")
else:
    print("No")
