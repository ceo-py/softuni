season = input()
kilometers = int(input())
kilometers_price = {
    "Spring": {
        "km_5000": 0.75,
        "km_5k_10k": 0.95,
        "km_more_than_10k": 1.45},
    "Summer": {
        "km_5000": 0.90,
        "km_5k_10k": 1.10,
        "km_more_than_10k": 1.45},
    "Winter": {
        "km_5000": 1.05,
        "km_5k_10k": 1.25,
        "km_more_than_10k": 1.45},
}
kilometers_range = None
if kilometers <= 5000:
    kilometers_range = "km_5000"
elif 5000 < kilometers <= 10000:
    kilometers_range = "km_5k_10k"
else:
    kilometers_range = "km_more_than_10k"
total = ((kilometers_price["Spring" if season == "Autumn" else season][
              kilometers_range] * kilometers) * 4) * 0.9
print(f"{total:.2f}")
