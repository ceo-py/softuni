contract_term = input()
contract_type = input()
mobile_internet = input()
mounts_to_pay = int(input())

tax_to_pay = 0

if contract_term == "one":
    if contract_type == "Small":
        tax_to_pay = 9.98

    elif contract_type == "Middle":
        tax_to_pay = 18.99

    elif contract_type == "Large":
        tax_to_pay = 25.98

    elif contract_type == "ExtraLarge":
        tax_to_pay = 35.99

elif contract_term == "two":
    if contract_type == "Small":
        tax_to_pay = 8.58

    elif contract_type == "Middle":
        tax_to_pay = 17.09

    elif contract_type == "Large":
        tax_to_pay = 23.59

    elif contract_type == "ExtraLarge":
        tax_to_pay = 31.79

if mobile_internet == "yes":
    if tax_to_pay <= 10:
        tax_to_pay += 5.50

    elif tax_to_pay <= 30:
        tax_to_pay += 4.35

    elif tax_to_pay > 30:
        tax_to_pay += 3.85

total_price_to_pay = tax_to_pay * mounts_to_pay

if contract_term == "two":
    total_price_to_pay = (tax_to_pay * mounts_to_pay) - ((tax_to_pay * mounts_to_pay) * 0.0375)

else:
    total_price_to_pay = tax_to_pay * mounts_to_pay

print(f"{total_price_to_pay:.2f} lv.")
