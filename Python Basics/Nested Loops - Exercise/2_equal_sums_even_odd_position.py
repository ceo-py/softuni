number_one = int(input())
number_two = int(input())


for number in range(number_one, number_two + 1):

    odd_sum = 0
    even_sum = 0
    number = str(number)

    for i in range(len(number)):
        num = int(number[i])

        if i % 2 == 0:
            even_sum += num

        else:
            odd_sum += num

    if odd_sum == even_sum:
        print(number, end=' ')




# number_one = int(input())
# number_two = int(input())
#
# for number in range(number_one, number_two + 1):
#     number_to_str = str(number)
#     even_sum = 0
#     odd_sum = 0
#
#     for index, digit in enumerate(number_to_str):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#     if even_sum == odd_sum:
#         print(number, end=" ")





# six_num_s = int(input())
# six_num_e = int(input())
# for num in range(six_num_s, six_num_e + 1):
#     num_l = list(map(int, str(num)))
#     odd_sum = num_l[0] + num_l[2] + num_l[4]
#     even_sum = num_l[1] + num_l[3] + num_l[5]
#     if odd_sum == even_sum:
#         print(num ,end=" ")






# [print(num, end=" ") for num in range(int(input()), int(input()) + 1) if sum(list(map(int, str(num)))[::2]) == sum(list(map(int, str(num)))[1::2])]




###
# number_one = int(input())
# number_two = int(input())
#
# for number in range(number_one, number_two + 1):
#     even_sum = 0
#     odd_sum = 0
#     for i, digit in enumerate(str(number)):
#         if i % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#     if even_sum == odd_sum:
#         print(number, end=" ")