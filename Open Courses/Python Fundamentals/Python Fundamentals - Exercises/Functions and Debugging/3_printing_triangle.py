number = int(input())


def create_triangle(n):
    start_num = 1
    for num in range(1, n + 1):
        print(start_num, end=" ")
        if num <= n:
            for num_one in range(2, num + 1):
                print(num_one, end=" ")
            print()
    for num in range(0, n - 1):
        print(start_num, end=" ")
        if num <= n:
            for num_one in range(2, n - num):
                print(num_one, end=" ")
            print()


create_triangle(number)
