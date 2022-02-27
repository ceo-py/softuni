type_flower = input()
count_flowers = int(input())
budget = int(input())

flowers = {"type": {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50, },
    "discount": {
        "Roses": 0.10,
        "Dahlias": 0.15,
        "Tulips": 0.15,
        "Narcissus": 0.15,
        "Gladiolus": 0.20}
}
over_eighty_discount = ("Roses", "Tulips")
over_ninth_discount = ("Dahlias",)
under_onehundred_twenty_discount = ("Narcissus",)
under_eighty_discount = ("Gladiolus",)

if count_flowers > 80 and type_flower in over_eighty_discount:
    total_value = count_flowers * flowers["type"][type_flower]
    discount_value = total_value - total_value * flowers["discount"][type_flower]
elif count_flowers > 90 and type_flower in over_ninth_discount:
    total_value = count_flowers * flowers["type"][type_flower]
    discount_value = total_value - total_value * flowers["discount"][type_flower]
elif count_flowers < 80 and type_flower in under_eighty_discount:
    total_value = count_flowers * flowers["type"][type_flower]
    discount_value = total_value + total_value * flowers["discount"][type_flower]
elif count_flowers < 120 and type_flower in under_onehundred_twenty_discount:
    total_value = count_flowers * flowers["type"][type_flower]
    discount_value = total_value + total_value * flowers["discount"][type_flower]
else:
    discount_value = count_flowers * flowers["type"][type_flower]
if budget >= discount_value:
    money_left = budget - discount_value
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {money_left:.2f} leva left.")
else:
    money_need = discount_value - budget
    print(f"Not enough money, you need {money_need:.2f} leva more.")
