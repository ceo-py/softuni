day_of_the_week = input()

output = 16

if day_of_the_week in 'Monday, Tuesday, Friday':
    output = 12

elif day_of_the_week in 'Wednesday, Thursday':
    output = 14

print(output)


# day_of_the_week = input()
#
# week = {
#     "Monday": 12,
#     "Tuesday": 12,
#     "Wednesday": 14,
#     "Thursday": 14,
#     "Friday": 12,
#     "Saturday": 16,
#     "Sunday": 16
# }
#
# print(week[day_of_the_week])
