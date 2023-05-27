days_of_vacation = int(input())
type_of_room = input()
grade = input()

nights_on_vacation = days_of_vacation - 1

price = 0
discount = 1
total_price = 0

ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

if type_of_room == 'room for one person':
    price = nights_on_vacation * ROOM_FOR_ONE_PERSON


elif type_of_room == 'apartment':
    price = nights_on_vacation * APARTMENT
    if days_of_vacation < 10:
        discount = 0.70
    elif 10 <= nights_on_vacation <= 15:
        discount = 0.65
    elif nights_on_vacation > 15:
        discount = 0.50

elif type_of_room == 'president apartment':
    price = nights_on_vacation * PRESIDENT_APARTMENT
    if nights_on_vacation < 10:
        discount = 0.90
    elif 10 == nights_on_vacation <= 15:
        discount = 0.85
    elif nights_on_vacation > 15:
        discount = 0.80

if grade == 'positive':
    price = (price + price * 0.25) * discount
elif grade == 'negative':
    price = (price - price * 0.10) * discount

print(f"{price:.2f}")






# days_stay = int(input()) - 1
# type_room = input()
# feed_back = input()
#
# rooms_info = {"less 10 days off": {
#     "room for one person": 0.00,
#     "apartment": 0.30,
#     "president apartment": 0.10},
#     "10 - 15 off": {
#         "room for one person": 0.00,
#         "apartment": 0.35,
#         "president apartment": 0.15},
#     "over 15 off": {
#         "room for one person": 0.00,
#         "apartment": 0.50,
#         "president apartment": 0.20},
#     "prices": {
#         "room for one person": 18.00,
#         "apartment": 25.00,
#         "president apartment": 35.00},
#     "feedback": {
#         "positive": 0.25,
#         "negative": 0.10}
#
# }
#
# if days_stay < 10 and not "room for one person" in type_room:
#     cost = (rooms_info["prices"][type_room] * days_stay)
#     cost = cost - (cost * rooms_info["less 10 days off"][type_room])
#     total = cost + (cost * rooms_info["feedback"][feed_back])
#     print("{:.2f}".format(total, 2))
# elif 10 <= days_stay <= 15 and not "room for one person" in type_room:
#     cost = (rooms_info["prices"][type_room] * days_stay)
#     cost = cost - (cost * rooms_info["10 - 15 off"][type_room])
#     total = cost + (cost * rooms_info["feedback"][feed_back])
#     print("{:.2f}".format(total, 2))
# elif days_stay > 15 and not "room for one person" in type_room:
#     cost = (rooms_info["prices"][type_room] * days_stay)
#     cost = cost - (cost * rooms_info["over 15 off"][type_room])
#     if feed_back == "positive":
#         total = cost + (cost * rooms_info["feedback"][feed_back])
#         print("{:.2f}".format(total, 2))
#     else:
#         total = cost - (cost * rooms_info["feedback"][feed_back])
#         print("{:.2f}".format(total, 2))
# else:
#     cost = rooms_info["prices"][type_room] * days_stay
#     total = cost + (cost * rooms_info["feedback"][feed_back])
#     print("{:.2f}".format(total, 2))
#
