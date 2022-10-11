number = input()
min_number = int(number)

while number != "Stop":
    num = int(number)

    if num < min_number:
        min_number = num
    number = input()

print(min_number)



#
# total = list()
# while True:
#     numbers = input()
#     if numbers != "Stop":
#         total.append(int(numbers))
#     else:
#         total.sort()
#         print(total[0])
#         break
