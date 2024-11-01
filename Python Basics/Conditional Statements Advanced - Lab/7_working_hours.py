hour = int(input())
day = input()

if 10 <= hour <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")



# hour = int(input())
# day_of_week = input()
# result = "closed"
#
# if 10 <= hour <= 18 and (day_of_week == "Monday" or
#             day_of_week == "Tuesday" or
#             day_of_week == "Wednesday" or
#             day_of_week == "Thursday" or
#             day_of_week == "Friday" or
#             day_of_week == "Saturday"):
#         result = "open"
#
# print(result)

# # Преход от това
# hour = int(input())
# day = input()
# ouput = "closed"
#
# if 10 <= hour <= 18 and day != "Sunday":
#     ouput = "open"
#
# print(ouput)


# # към това
# hour = int(input())
# day = input()
# ouput = "closed" if 10 <= hour <= 18 and day != "Sunday" else "closed"
# print(ouput)



# # до това
# print("closed" if 10 <= int(input()) <= 18 and input() != "Sunday" else "closed")


# hour = int(input())
# day_of_the_week = input()
#
# week = {
#     "Monday": "open",
#     "Tuesday": "open",
#     "Wednesday": "open",
#     "Thursday": "open",
#     "Friday": "open",
#     "Saturday": "open",
#     "Sunday": "closed"
# }
#
# if hour in range(10, 19):
#     print(week[day_of_the_week])
# else:
#     print(week["Sunday"])
