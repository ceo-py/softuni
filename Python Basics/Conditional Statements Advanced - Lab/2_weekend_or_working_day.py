day = input()

output = 'Error'

if day in 'Monday, Tuesday, Wednesday, Thursday, Friday':
    output = 'Working day'

elif day in 'Saturday, Sunday':
    output = 'Weekend'


print(output)



# check_what_day_is = input()
#
# week = {
#     "Monday": "Working day",
#     "Tuesday": "Working day",
#     "Wednesday": "Working day",
#     "Thursday": "Working day",
#     "Friday": "Working day",
#     "Saturday": "Weekend",
#     "Sunday": "Weekend",
#
# }
#
# print(week.get(check_what_day_is, 'Error'))





#
# result = {
# "Monday": "Working day", "Tuesday": "Working day", "Wednesday": "Working day", "Thursday": "Working day",
#     "Friday": "Working day","Saturday": "Weekend", "Sunday": "Weekend"}
# print(result.get(input(), "Error"))
#
