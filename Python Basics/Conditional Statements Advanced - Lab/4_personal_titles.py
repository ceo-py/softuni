person_age = float(input())
person_sex = input()

title_check = {
    "m under 16": "Master",
    "m over 16": "Mr.",
    "f under 16": "Miss",
    "f over 16": "Ms."
}

if person_sex == "m":
    if person_age < 16:
        print(title_check["m under 16"])
    else:
        print(title_check["m over 16"])
elif person_sex == "f":
    if person_age < 16:
        print(title_check["f under 16"])
    else:
        print(title_check["f over 16"])
