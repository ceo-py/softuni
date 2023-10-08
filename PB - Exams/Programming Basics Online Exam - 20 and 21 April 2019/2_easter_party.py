number_guests = int(input())
reservation_one_person = float(input())
budget = float(input())

cake_price = budget * 0.10
discount = 0

if number_guests < 10:
    discount = 1

elif 10 <= number_guests <= 15:
    discount = 0.85

elif number_guests <= 20:
    discount = 0.80

elif number_guests > 20:
    discount = 0.75

expenses = ((number_guests * reservation_one_person) * discount) + cake_price
total_sum = budget - expenses

if total_sum >= 0:
    print(f'It is party time! {total_sum:.2f} leva left.')
else:
    print(f'No party! {abs(total_sum):.2f} leva needed.')







# guest_numbers = int(input())
# price_reservation = float(input())
# budget = float(input())
#
# off_reservation = 0
#
# if guest_numbers < 10:
#     off_reservation = price_reservation
#
# elif guest_numbers <= 15:
#     off_reservation = price_reservation - (price_reservation * 0.15)
#
# elif guest_numbers <= 20:
#     off_reservation = price_reservation - (price_reservation * 0.20)
#
# elif guest_numbers > 20:
#     off_reservation = price_reservation - (price_reservation * 0.25)
#
# cake = budget - (budget * 0.90)
# total = (off_reservation * guest_numbers) + cake
# money_left = abs(budget - total)
#
# if total <= budget:
#     print(f"It is party time! {money_left:.2f} leva left.")
#
# else:
#     print(f"No party! {money_left:.2f} leva needed.")
