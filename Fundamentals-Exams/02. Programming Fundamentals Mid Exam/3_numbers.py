main_list = [int(x) for x in input().split()]
average_number = sum(main_list) / len(main_list)
main_list.sort(reverse=True)
print_numbers = False

for index, number in enumerate(main_list):
    if index <= 4 and number > average_number:
        print(number, end=" ")
        print_numbers = True
    if not print_numbers:
        print("No")
        break
