days_of_the_week = int(input())

week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if days_of_the_week in range(1, 8):
    print(week[days_of_the_week])
else:
    print("Error")
