a = float(input())

if a <= 10:
    print("slow")
elif a <= 50:
    print("average")
elif a <= 150:
    print("fast")
elif a <= 1000:
    print("ultra fast")
else:
    print("extremely fast")