serial_budget = float(input())
serial_numbers = int(input())

serial_info = {
    "Thrones": 0.50,
    "Lucifer": 0.60,
    "Protector": 0.70,
    "TotalDrama": 0.80,
    "Area": 0.90
}
serial_count = 0
total_budget = serial_budget

while True:
    name_serial = input()
    price_serial = float(input())
    serial_count += 1
    if name_serial in serial_info:
        total_budget = total_budget - (serial_info[name_serial] * price_serial)

    else:
        total_budget = total_budget - price_serial

    if serial_numbers == serial_count and total_budget >= 0:
        print(f"You bought all the series and left with {total_budget:.2f} lv.")
        break

    elif total_budget < 0 and serial_count == serial_numbers:
        print(f"You need {abs(total_budget):.2f} lv. more to buy the series!")
        break
