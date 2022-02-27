town_name = input()
sales = float(input())

commisions_town = {"Sofia": {
    "500": 0.05,
    "over 500 - 1000": 0.07,
    "1000 - 10000": 0.08,
    "over 10000": 0.12, },
    "Varna": {
        "500": 0.045,
        "over 500 - 1000": 0.075,
        "1000 - 10000": 0.10,
        "over 10000": 0.13, },
    "Plovdiv": {
        "500": 0.055,
        "over 500 - 1000": 0.08,
        "1000 - 10000": 0.12,
        "over 10000": 0.145, }
}

if town_name in commisions_town and sales > 0:
    if 0 <= sales <= 500:
        total_sales = commisions_town[town_name]["500"] * sales
    elif 500 < sales <= 1000:
        total_sales = commisions_town[town_name]["over 500 - 1000"] * sales
    elif 1000 < sales <= 10000:
        total_sales = commisions_town[town_name]["1000 - 10000"] * sales
    elif sales > 10000:
        total_sales = commisions_town[town_name]["over 10000"] * sales
    print("{:.2f}".format((total_sales)))

else:
    print("error")
