n = int(input())

if n > 1:
    for i in range(2, n // 2):
        if (n % i) == 0:
            print("False")
            break
    else:
        print("True")

