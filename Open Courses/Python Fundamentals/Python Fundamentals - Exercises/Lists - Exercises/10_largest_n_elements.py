main_list = [int(x) for x in input().split()]
numbers = int(input())
main_list.sort(reverse=True)
for i in range(numbers):
    print(f"{main_list[i]}", end = " ")