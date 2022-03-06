# numbers = input()
#
# lst = numbers.split(' ')
# new_list = list()
# for number in lst:
#
#     if number[0] == "-":
#         new_list.append(abs((int(number))))
#     else:
#         new_number = int(str("-" + number))
#         new_list.append(new_number)
#
# print(new_list)


numbers = input()

lst = numbers.split(' ')
new_list = list()

for number in lst:
    main_string = int(number) * -1
    new_list.append(main_string)

print(new_list)
