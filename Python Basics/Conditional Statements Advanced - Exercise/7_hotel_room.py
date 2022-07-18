month = input()
amount_overnights = int(input())

total_price_apartment = 0
total_price_studio = 0
discount_studio = 1
discount_apartment = 1

if month == "May" or month == "October":
    total_price_studio = 50
    total_price_apartment = 65

    if 7 < amount_overnights <= 14:
        discount_studio = .95

    if amount_overnights > 14:
        discount_studio = .7

elif month == "June" or month == "September":
    total_price_studio = 75.20
    total_price_apartment = 68.70

    if amount_overnights > 14:
        discount_studio *= .8

elif month == "July" or month == "August":
    total_price_studio = 76
    total_price_apartment = 77

if amount_overnights > 14:
    discount_apartment = .9

total_price_studio = (total_price_studio * amount_overnights) * discount_studio
total_price_apartment = (total_price_apartment * amount_overnights) * discount_apartment

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")





#
#
# month = input()
# number_days = int(input())
#
# accomodation = {"May": {
#         "Studio": 50.00,
#         "Apartment": 65.00},
#     "October": {
#         "Studio": 50.00,
#         "Apartment": 65.00},
#     "June": {
#         "Studio": 75.20,
#         "Apartment": 68.70},
#     "September": {
#         "Studio": 75.20,
#         "Apartment": 68.70},
#     "July": {
#         "Studio": 76.00,
#         "Apartment": 77.00},
#     "August": {
#         "Studio": 76.00,
#         "Apartment": 77.00},
# }
#
# studio_price = accomodation[month]["Studio"] * number_days
# apartment_price = accomodation[month]["Apartment"] * number_days
#
# if month == "May" or month == "October":
#     if 7 < number_days <= 14:
#         studio_price = studio_price - (studio_price * 0.05)
#         apartment_price = accomodation[month]["Apartment"] * number_days
#     if number_days > 14:
#         studio_price = studio_price - (studio_price * 0.3)
#
# elif month == "June" or month == "September":
#     if number_days > 14:
#         studio_price = studio_price - (studio_price * 0.2)
# if number_days > 14:
#     apartment_price = apartment_price - (apartment_price * 0.1)
#
# print(f"Apartment: {apartment_price:.2f} lv.")
# print(f"Studio: {studio_price:.2f} lv.")
#
#


#
#
# month = input()
# sleep_count = int(input())
#
# hotel_info = {"May": {
#     "7 sleeps 5%": 0.05,
#     "14 sleeps": 0.30,
#     "Apartment": 65,
#     "Studio": 50, },
#     "October": {
#         "7 sleeps 5%": 0.05,
#         "14 sleeps": 0.30,
#         "Apartment": 65,
#         "Studio": 50, },
#     "June": {
#         "14 sleeps": 0.20,
#         "Apartment": 68.70,
#         "Studio": 75.20, },
#     "September": {
#         "14 sleeps": 0.20,
#         "Apartment": 68.70,
#         "Studio": 75.20, },
#     "July": {
#         "Apartment": 77,
#         "Studio": 76, },
#     "August": {
#         "Apartment": 77,
#         "Studio": 76, },
#     "Apartment discount": {
#         "14 sleeps 10%": 0.10, },
# }
# month_off_fourteen_over = ("May", "October", "June", "September")
# mothn_off_seven_days = ("May", "October")
# studio = hotel_info[month]["Studio"] * sleep_count
# apartment = hotel_info[month]["Apartment"] * sleep_count
#
# if 14 >= sleep_count > 7 and month in mothn_off_seven_days:
#     apartment = hotel_info[month]["Apartment"] * sleep_count
#     studio = (hotel_info[month]["Studio"] - (hotel_info[month]["Studio"]
#             * hotel_info[month]["7 sleeps 5%"])) * sleep_count
# elif sleep_count > 14 and month in month_off_fourteen_over:
#     apartment = (hotel_info[month]["Apartment"] - (hotel_info[month]["Apartment"]
#                 * hotel_info["Apartment discount"]["14 sleeps 10%"])) * sleep_count
#     studio = (hotel_info[month]["Studio"] - (hotel_info[month]["Studio"]
#                 * hotel_info[month]["14 sleeps"])) * sleep_count
# elif sleep_count > 14 and month not in month_off_fourteen_over:
#     apartment = (hotel_info[month]["Apartment"] - (hotel_info[month]["Apartment"]
#                 * hotel_info["Apartment discount"]["14 sleeps 10%"])) * sleep_count
#     studio = hotel_info[month]["Studio"] * sleep_count
#
#
# print(f"Apartment: {apartment:.2f} lv.")
# print(f"Studio: {studio:.2f} lv.")
