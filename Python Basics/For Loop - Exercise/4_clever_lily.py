lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

added_money_to_birthday_eve = 0
brother_steal_money = 1
extra_money = 0
gifts_received = -1

for age in range(0, lily_age + 1):
    if age != 0 and (age % 2) == 0:
        added_money_to_birthday_eve += 10
        extra_money += added_money_to_birthday_eve
    else:
        gifts_received += 1

total_brother_steal_money = brother_steal_money * (lily_age - gifts_received)
extra_money = (extra_money + (gifts_received * toy_price)) - total_brother_steal_money

if extra_money >= washing_machine_price:
    extra_money = extra_money - washing_machine_price
    print(f"Yes! {extra_money:.2f}")
else:
    extra_money = washing_machine_price - extra_money
    print(f"No! {extra_money:.2f}")
