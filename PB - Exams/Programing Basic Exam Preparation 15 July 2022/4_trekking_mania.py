number_claiming_group = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group in range(number_claiming_group):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimanjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

total_people = musala + monblan + kilimanjaro + k2 + everest

percent_musala = musala / total_people * 100
percent_monblan = monblan / total_people * 100
percent_kilimanjaro = kilimanjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
