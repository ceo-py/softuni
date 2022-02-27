guest_numbers = int(input())
price_reservation = float(input())
budget = float(input())

off_reservation = 0

if guest_numbers < 10:
    off_reservation = price_reservation

elif guest_numbers <= 15:
    off_reservation = price_reservation - (price_reservation * 0.15)

elif guest_numbers <= 20:
    off_reservation = price_reservation - (price_reservation * 0.20)

elif guest_numbers > 20:
    off_reservation = price_reservation - (price_reservation * 0.25)

cake = budget - (budget * 0.90)
total = (off_reservation * guest_numbers) + cake
money_left = abs(budget - total)

if total <= budget:
    print(f"It is party time! {money_left:.2f} leva left.")

else:
    print(f"No party! {money_left:.2f} leva needed.")
