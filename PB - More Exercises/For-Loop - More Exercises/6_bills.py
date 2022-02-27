months = int(input())

electricity_bill = 0
water_bill = 20
internet = 15
others = 0
bills_count = 0

for _ in range(1, months + 1):
    electricity_bill_mount = float(input())
    electricity_bill += electricity_bill_mount
    others += (electricity_bill_mount + water_bill + internet) + (electricity_bill_mount + water_bill + internet) * 0.20
    bills_count += 1

internet = internet * months
water_bill = water_bill * months
average_bill = (electricity_bill + water_bill + internet + others) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
