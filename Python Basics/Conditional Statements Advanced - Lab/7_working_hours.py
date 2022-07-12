hour = int(input())
day = input()

if 10 <= hour <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")




#
#
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
