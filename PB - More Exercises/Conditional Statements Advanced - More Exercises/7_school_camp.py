season = input()
group_type = input()
number_studens = int(input())
number_sleeps = int(input())

vacantion_info = {
    "Winter": {
        "boys": "Judo",
        "girls": "Gymnastics",
        "mixed": "Ski"},
    "Spring": {
        "boys": "Tennis",
        "girls": "Athletics",
        "mixed": "Cycling"},
    "Summer": {
        "boys": "Football",
        "girls": "Volleyball",
        "mixed": "Swimming"},
    "price": {
        "Winter": [9.60, 10],
        "Spring": [7.20, 9.5],
        "Summer": [15, 20]}}

discount = 1
if 10 <= number_studens < 20:
    discount = 0.95
elif 20 <= number_studens < 50:
    discount = 0.85
elif number_studens >= 50:
    discount = 0.50

total_price = ((vacantion_info["price"][season][
                    0 if group_type != "mixed" else 1] * number_sleeps) * number_studens) * discount
print(f"{vacantion_info[season][group_type]} {total_price:.2f} lv.")

