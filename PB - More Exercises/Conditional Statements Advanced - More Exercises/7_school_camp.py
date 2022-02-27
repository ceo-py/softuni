season = input()
group_type = input()
number_studens = int(input())
number_sleeps = int(input())

vacantion_info = {
    1: {
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
            "Winter": 9.60,
            "Spring": 7.20,
            "Summer": 15},
        "mixed": {
            "Winter": 10,
            "Spring": 9.5,
            "Summer": 20}}}

if 0 <= number_studens < 10 and group_type == "mixed":
    total_price = (vacantion_info[1]["mixed"][season] * number_sleeps) * number_studens
elif 10 <= number_studens < 20 and group_type == "mixed":
    total_price = (vacantion_info[1]["mixed"][season] * number_sleeps) * number_studens
    total_price += - (total_price * 0.05)
elif number_studens < 50 and group_type == "mixed":
    total_price = (vacantion_info[1]["mixed"][season] * number_sleeps) * number_studens
    total_price += - (total_price * 0.15)
elif number_studens >= 50 and group_type == "mixed":
    total_price = (vacantion_info[1]["mixed"][season] * number_sleeps) * number_studens
    total_price += - (total_price * 0.50)
elif 0 <= number_studens < 10:
    total_price = (vacantion_info[1]["price"][season] * number_sleeps) * number_studens
elif 10 <= number_studens < 20:
    total_price = (vacantion_info[1]["price"][season] * number_sleeps) * number_studens
    total_price += - (total_price * 0.05)
elif number_studens < 50:
    total_price = (vacantion_info[1]["price"][season] * number_sleeps) * number_studens
    total_price += - (total_price * 0.15)
elif number_studens >= 50:
    total_price = (vacantion_info[1]["price"][season] * number_sleeps) * number_studens
    total_price += - (total_price * 0.50)

print(f"{vacantion_info[1][season][group_type]} {total_price:.2f} lv.")
