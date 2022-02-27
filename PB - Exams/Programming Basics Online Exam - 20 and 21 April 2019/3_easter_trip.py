holiday_destination = input()
dates_for_reservation = input()
number_sleep_over = int(input())

holiday_info = {
    "21-23": {
        "France": 30,
        "Italy": 28,
        "Germany": 32},
    "24-27": {
        "France": 35,
        "Italy": 32,
        "Germany": 37},
    "28-31": {
        "France": 40,
        "Italy": 39,
        "Germany": 43},

}

total = holiday_info[dates_for_reservation][holiday_destination] * number_sleep_over

print(f"Easter trip to {holiday_destination} : {total:.2f} leva.")