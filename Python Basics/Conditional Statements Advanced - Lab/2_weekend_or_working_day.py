check_what_day_is = input()




week = {
    "Monday": "Working day",
    "Tuesday": "Working day",
    "Wednesday": "Working day",
    "Thursday": "Working day",
    "Friday": "Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend",

}

if check_what_day_is in week:
    print(week[check_what_day_is])
else:
    print("Error")
