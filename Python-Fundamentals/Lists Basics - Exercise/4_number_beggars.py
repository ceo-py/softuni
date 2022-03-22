first_line = input()
second_line = int(input())

first_line = first_line.split(",")
total_list = list()
old_list = list()
length_of_first = len(first_line)

if length_of_first < second_line:
    for number in first_line:
        total_list.append(int(number))
    for number in range(abs(length_of_first - second_line)):
        total_list.append(0)


elif length_of_first == second_line:
    for number in first_line:
        total_list.append(int(number))

else:
    for number in first_line:
        old_list.append(int(number))
    for _ in range(0, second_line):
        total_list.append(sum(old_list[_::second_line]))

print(total_list)
