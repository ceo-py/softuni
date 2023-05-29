numbers = [int(input()) for _ in range(int(input()))]
command = input()
print([x for x in numbers if any([command == "odd" and x % 2 != 0, command == "even" and x % 2 ==0,command == "positive" and x >= 0, command == "negative" and x < 0])])




# numbers = [int(input()) for _ in range(int(input()))]
# data_ = {
# 	"odd": [x for x in numbers if x % 2 != 0],
# 	"even": [x for x in numbers if x % 2 == 0],
# 	"positive": [x for x in numbers if x >= 0],
# 	"negative": [x for x in numbers if x < 0]
# }
# print(data_[input()])




# num = int(input())
# data_ = {
# 	"odd": [],
# 	"even": [],
# 	"positive": [],
# 	"negative": []
# }
# for i in range(num):
#     number = int(input())
#     if number % 2 != 0:
#             data_["odd"].append(number)
#     if number % 2 == 0:
#             data_["even"].append(number)
#     if number >= 0:
#             data_["positive"].append(number)
#     else:
#     	    data_["negative"].append(number)
#
#
# print(data_[input()])






#
# number_range = int(input())
#
# even = list()
# negative = list()
# positive = list()
# odd = list()
#
# for _ in range(1, number_range + 2):
#     number = input()
#
#     if number == "even":
#         break
#     elif number == "negative":
#         break
#
#     elif number == "positive":
#         break
#
#     elif number == "odd":
#         break
#
#     if int(number) % 2 == 0:
#         even.append(int(number))
#
#     if int(number) < 0:
#         negative.append(int(number))
#
#     if int(number) >= 0:
#         positive.append(int(number))
#
#     if int(number) % 2 != 0:
#         odd.append(int(number))
#
# if number == "even":
#     print(even)
#
# elif number == "negative":
#     print(negative)
#
# elif number == "positive":
#     print(positive)
#
# elif number == "odd":
#     print(odd)
#


