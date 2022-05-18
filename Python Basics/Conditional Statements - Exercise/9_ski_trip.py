days = int(input())
type_of_room = input()
score = input()
room_for_one_person, apartment, president_apartment = 18, 25, 35
discount, price, final_price = 0, 0, 0

if days >= 1:
    days = days - 1
if type_of_room == "room for one person":
    price = room_for_one_person * days
elif type_of_room == "apartment":
    if days < 10:
        discount = 0.7
    elif 10 <= days <= 15:
        discount = 0.65
    elif days > 15:
        discount = 0.5
    price = (apartment * discount) * days
elif type_of_room == "president apartment":
    if days < 10:
        discount = 0.9
    elif 10 <= days <= 15:
        discount = 0.85
    elif days > 15:
        discount = 0.80
    price = (president_apartment * discount) * days
if score == 'positive':
    final_price = price * 1.25
elif score == 'negative':
    final_price = price * 0.90
print(f'{final_price:.2f}')





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

