window_frames_number = int(input())
window_frames_type = input()
delivery_type = input()

single_price = 0
discount = 1
output = 'Invalid order'

if window_frames_type == '90X130':
    single_price = 110
    if window_frames_number > 60:
        discount = 0.92
    elif window_frames_number > 30:
        discount = 0.95

elif window_frames_type == '100X150':
    single_price = 140
    if window_frames_number > 80:
        discount = 0.90
    elif window_frames_number > 40:
        discount = 0.94

elif window_frames_type == '130X180':
    single_price = 190
    if window_frames_number > 50:
        discount = 0.88
    elif window_frames_number > 20:
        discount = 0.93

elif window_frames_type == '200X300':
    single_price = 250
    if window_frames_number > 50:
        discount = 0.86
    elif window_frames_number > 25:
        discount = 0.91


if window_frames_number > 10:
    output = single_price * window_frames_number * discount

    if delivery_type == 'With delivery':
        output += 60

    if window_frames_number > 99:
        output *= 0.96

    output = f'{output:.2f} BGN'

print(output)




# window_count = int(input())
# window_type = str(input())
# delivery = str(input())
# window_price = float()
# total_cost_before_discount = float()
# transport_cost = float()
# stop_under_order = False
#
# if window_count < 10:
#     print("Invalid order")
#
# if window_type == "90X130" and window_count <= 30:
#     window_price = 110
# elif window_type == "90X130" and window_count <= 60:
#     window_price = 110 * 0.95
# elif window_type == "90X130" and window_count > 60:
#     window_price = 110 * 0.92
# elif window_type == "100X150" and window_count <= 40:
#     window_price = 140
# elif window_type == "100X150" and window_count <= 80:
#     window_price = 140 * 0.94
# elif window_type == "100X150" and window_count > 80:
#     window_price = 140 * 0.90
# elif window_type == "130X180" and window_count <= 20:
#     window_price = 190
# elif window_type == "130X180" and window_count <= 50:
#     window_price = 190 * 0.93
# elif window_type == "130X180" and window_count > 50:
#     window_price = 190 * 0.88
# elif window_type == "200X300" and window_count <= 25:
#     window_price = 250
# elif window_type == "200X300" and window_count <= 50:
#     window_price = 250 * 0.91
# elif window_type == "200X300" and window_count > 50:
#     window_price = 250 * 0.86
# total_cost_before_discount = window_count * window_price + transport_cost
# if delivery == "With delivery":
#     transport_cost = 60
# elif delivery == "Without delivery":
#     transport_cost = 0
# if window_count >= 99:
#     total_cost_before_discount = (total_cost_before_discount + transport_cost) * 0.96
# else:
#     total_cost_before_discount = total_cost_before_discount + transport_cost
# result = "{:.2f}".format(total_cost_before_discount)
# if window_count >= 10:
#     print(f"{result} BGN")



#
#
# number_joinery = int(input())
# joinery_type = input()
# deliver = input()
#
# joinery_size_ninety = 110
# joinery_size_onehundred = 140
# joinery_size_onehundred_thurty = 190
# joinery_size_twohundred = 250
# delivery_fee = 60
#
# if number_joinery < 10:
#     print("Invalid order")
#     stop_under_order = False
#
# else:
#
#     if "90X130" == joinery_type:
#         if number_joinery <= 30:
#             joinery_price_off = number_joinery * joinery_size_ninety
#
#         if number_joinery > 30:
#             joinery_price_off = number_joinery * joinery_size_ninety
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.05
#
#         if number_joinery > 60:
#             joinery_price_off = number_joinery * joinery_size_ninety
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.08
#
#     elif "100X150" == joinery_type:
#         if number_joinery <= 40:
#             joinery_price_off = number_joinery * joinery_size_onehundred
#
#         if number_joinery > 40:
#             joinery_price_off = number_joinery * joinery_size_onehundred
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.06
#
#         if number_joinery > 80:
#             joinery_price_off = number_joinery * joinery_size_onehundred
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.10
#
#     elif "130X180" == joinery_type:
#         if number_joinery <= 20:
#             joinery_price_off = number_joinery * joinery_size_onehundred_thurty
#
#         if number_joinery > 20:
#             joinery_price_off = number_joinery * joinery_size_onehundred_thurty
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.07
#
#         if number_joinery > 50:
#             joinery_price_off = number_joinery * joinery_size_onehundred_thurty
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.12
#
#     elif "200X300" == joinery_type:
#         if number_joinery <= 25:
#             joinery_price_off = number_joinery * joinery_size_twohundred
#
#         if number_joinery > 25:
#             joinery_price_off = number_joinery * joinery_size_twohundred
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.09
#
#         if number_joinery > 50:
#             joinery_price_off = number_joinery * joinery_size_twohundred
#             joinery_price_off = joinery_price_off - joinery_price_off * 0.14
#
#     if "With delivery" == deliver:
#         joinery_price_off = joinery_price_off + delivery_fee
#
#     if "Without delivery" == deliver:
#         joinery_price_off = joinery_price_off
#
#     if number_joinery > 99:
#         joinery_price_off = joinery_price_off - joinery_price_off * 0.04
#
#     joinery_price_off = "{:.2f}".format(joinery_price_off)
#
#     print(f"{joinery_price_off} BGN")
