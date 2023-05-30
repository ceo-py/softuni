event = input()
ticket_type = input()
number_tickets = int(input())
picture_with_trophy = input()

ticket_price = 0
picture_with_trophy_price = 40

if ticket_type == "Standard":
    if "Quarter final" == event:
        ticket_price = 55.50
    elif "Semi final" == event:
        ticket_price = 75.88
    elif "Final" == event:
        ticket_price = 110.10

elif ticket_type == "Premium":
    if "Quarter final" == event:
        ticket_price = 105.20
    elif "Semi final" == event:
        ticket_price = 125.22
    elif "Final" == event:
        ticket_price = 160.66

elif ticket_type == "VIP":
    if "Quarter final" == event:
        ticket_price = 118.90
    elif "Semi final" == event:
        ticket_price = 300.40
    elif "Final" == event:
        ticket_price = 400


total_sum = ticket_price * number_tickets

if total_sum > 4_000:
    total_sum *= 0.75
    picture_with_trophy_price = 0
elif total_sum > 2_500:
    total_sum *= 0.90

if picture_with_trophy == "Y":
    total_sum += number_tickets * picture_with_trophy_price

print(f"{total_sum:.2f}")






#
#
# competitions_type = input()
# ticket_type = input()
# number_tickets = int(input())
# picture_with_trophy = input()
#
# tournament_info = {
#     "Quarter final": {
#         "Standard": 55.50,
#         "Premium": 105.20,
#         "VIP": 118.90},
#     "Semi final": {
#         "Standard": 75.88,
#         "Premium": 125.22,
#         "VIP": 300.40},
#     "Final": {
#         "Standard": 110.10,
#         "Premium": 160.66,
#         "VIP": 400},
# }
#
# total = tournament_info[competitions_type][ticket_type] * number_tickets
#
# if total > 4000 and picture_with_trophy == "Y":
#     total = (total - (total * 0.25))
#
# elif total > 2500 and picture_with_trophy == "Y":
#     total = total - (total * 0.10) + (40 * number_tickets)
#
# elif total > 4000 and picture_with_trophy == "N":
#     total = (total - (total * 0.25))
#
# elif total > 2500 and picture_with_trophy == "N":
#     total = (total - (total * 0.10))
#
# elif total <= 2500 and picture_with_trophy == "Y":
#     total += 40 * number_tickets
#
#
# print(f"{total:.2f}")



# competitions_type = input()
# ticket_type = input()
# number_tickets = int(input())
# picture_with_trophy = input()
#
# if competitions_type == "Quarter final":
#
#     if ticket_type == "Standard":
#
#         total = number_tickets * 55.50
#
#     elif ticket_type == "Premium":
#
#         total = number_tickets * 105.20
#
#     elif ticket_type == "VIP":
#
#         total = number_tickets * 118.90
#
#
# elif competitions_type == "Semi final":
#
#     if ticket_type == "Standard":
#
#         total = number_tickets * 75.88
#
#     elif ticket_type == "Premium":
#
#         total = number_tickets * 125.22
#
#     elif ticket_type == "VIP":
#
#         total = number_tickets * 300.40
#
# elif competitions_type == "Final":
#
#     if ticket_type == "Standard":
#
#         total = number_tickets * 110.10
#
#     elif ticket_type == "Premium":
#
#         total = number_tickets * 160.66
#
#     elif ticket_type == "VIP":
#
#         total = number_tickets * 400
#
# if total > 4000 and picture_with_trophy == "Y":
#     total = total - (total * 0.25)
#
# elif total > 4000 and picture_with_trophy == "N":
#     total = total - (total * 0.25)
#
# elif total > 2500 and picture_with_trophy == "Y":
#     total = total - (total * 0.10)
#     total = total + (40 * number_tickets)
#
# elif total > 2500 and picture_with_trophy == "N":
#     total = total - (total * 0.10)
#
# elif picture_with_trophy == "Y":
#     total = total + (40 * number_tickets)
#
# print(f"{total:.2f}")

