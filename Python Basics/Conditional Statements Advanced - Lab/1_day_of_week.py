days_of_the_week = input()

output = 'Error'

if days_of_the_week == '1':
    output = 'Monday'

elif days_of_the_week == '2':
    output = 'Tuesday'

elif days_of_the_week == '3':
    output = 'Wednesday'

elif days_of_the_week == '4':
    output = 'Thursday'

elif days_of_the_week == '5':
    output = 'Friday'

elif days_of_the_week == '6':
    output = 'Saturday'

elif days_of_the_week == '7':
    output = 'Sunday'

print(output)



# days_of_the_week = input()
#
# week = {
#     "1": "Monday",
#     "2": "Tuesday",
#     "3": "Wednesday",
#     "4": "Thursday",
#     "5": "Friday",
#     "6": "Saturday",
#     "7": "Sunday"
# }
#
# print(week.get(days_of_the_week, 'Error'))

