month = input()
sleep_count = int(input())

hotel_info = {"May": {
    "7 sleeps 5%": 0.05,
    "14 sleeps": 0.30,
    "Apartment": 65,
    "Studio": 50, },
    "October": {
        "7 sleeps 5%": 0.05,
        "14 sleeps": 0.30,
        "Apartment": 65,
        "Studio": 50, },
    "June": {
        "14 sleeps": 0.20,
        "Apartment": 68.70,
        "Studio": 75.20, },
    "September": {
        "14 sleeps": 0.20,
        "Apartment": 68.70,
        "Studio": 75.20, },
    "July": {
        "Apartment": 77,
        "Studio": 76, },
    "August": {
        "Apartment": 77,
        "Studio": 76, },
    "Apartment discount": {
        "14 sleeps 10%": 0.10, },
}
month_off_fourteen_over = ("May", "October", "June", "September")
mothn_off_seven_days = ("May", "October")
studio = hotel_info[month]["Studio"] * sleep_count
apartment = hotel_info[month]["Apartment"] * sleep_count

if 14 >= sleep_count > 7 and month in mothn_off_seven_days:
    apartment = hotel_info[month]["Apartment"] * sleep_count
    studio = (hotel_info[month]["Studio"] - (hotel_info[month]["Studio"]
            * hotel_info[month]["7 sleeps 5%"])) * sleep_count
elif sleep_count > 14 and month in month_off_fourteen_over:
    apartment = (hotel_info[month]["Apartment"] - (hotel_info[month]["Apartment"]
                * hotel_info["Apartment discount"]["14 sleeps 10%"])) * sleep_count
    studio = (hotel_info[month]["Studio"] - (hotel_info[month]["Studio"]
                * hotel_info[month]["14 sleeps"])) * sleep_count
elif sleep_count > 14 and month not in month_off_fourteen_over:
    apartment = (hotel_info[month]["Apartment"] - (hotel_info[month]["Apartment"]
                * hotel_info["Apartment discount"]["14 sleeps 10%"])) * sleep_count
    studio = hotel_info[month]["Studio"] * sleep_count


print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
