pin_one = int(input())
pin_two = int(input())
pin_three = int(input())

for num_one in range(1, pin_one + 1):
    for num_two in range(1, pin_two + 1):
        for num_three in range(1, pin_three + 1):
            if num_one % 2 == 0 and num_three % 2 == 0 and str(num_two) in "2357":
                print(f"{num_one} {num_two} {num_three}")



#thanks to  Nenogzar
# pin_one = int(input())
# pin_two = int(input())
# pin_three = int(input())
# for num_one in range(2, pin_one+1, 2):
#     for number_two in range(2, pin_two+1):
#         for num_tree in range(2, pin_three+1, 2):
#             if str(number_two) in "2357":
#                 print(num_one, number_two, num_tree)



# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# for i in range(1, num_1 + 1):
#     if i % 2 == 0:
#         for j in range(1, num_2 + 1):
#             if str(j) in '2357':
#                 for h in range(1, num_3 + 1):
#                     if h % 2 == 0:
#                         print(i, j, h)




# pin_one = int(input())
# pin_two = int(input())
# pin_three = int(input())
#
# for number_one in range(2, pin_one + 1):
#     if number_one % 2 == 0:
#
#         for number_two in range(2, pin_two + 1):
#             prime_numbers = True
#
#             for i in range(2, number_two):
#                 if number_two % i == 0:
#                     prime_numbers = False
#                     break
#
#             if prime_numbers:
#                 for number_three in range(2, pin_three + 1):
#                     if number_three % 2 == 0:
#                         print(f"{number_one} {number_two} {number_three}")