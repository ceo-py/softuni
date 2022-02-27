budget = float(input())
fuel_needed = float(input())
day_of_the_week = input()

fuel_price = fuel_needed * 2.10
total_price = fuel_price + 100

if day_of_the_week == "Saturday":
    total_price += - (total_price * 0.10)

elif day_of_the_week == "Sunday":
    total_price += - (total_price * 0.20)

money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"Safari time! Money left: {money_left:.2f} lv. ")

else:
    print(f"Not enough money! Money needed: {money_left:.2f} lv.")
