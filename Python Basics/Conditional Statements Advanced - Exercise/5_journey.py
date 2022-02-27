budget = float(input())
weather_season = input()

budget_info = {100: {
    1: "Bulgaria",
    "summer": 0.30,
    "winter": 0.70, },
    1000: {
        1: "Balkans",
        "summer": 0.40,
        "winter": 0.80, },
    1001: {
        1: "Europe",
        "summer": 0.90,
        "winter": 0.90, },
    1: {
        "summer": "Camp",
        "winter": "Hotel"
    }

}

if budget <= 100:
    money_left = budget * budget_info[100][weather_season]
    print(f"Somewhere in {budget_info[100][1]}\n{budget_info[1][weather_season]} - {money_left:.2f}")
elif budget <= 1000:
    money_left = budget * budget_info[1000][weather_season]
    print(f"Somewhere in {budget_info[1000][1]}\n{budget_info[1][weather_season]} - {money_left:.2f}")
elif budget > 1000:
    money_left = budget * budget_info[1001][weather_season]
    print(f"Somewhere in Europe\nHotel - {money_left:.2f}")
