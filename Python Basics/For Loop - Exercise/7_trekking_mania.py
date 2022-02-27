number_groups = int(input())

five_people_gorups = 0
six_to_twelve_groups = 0
thirteen_people_gorups = 0
twenty_six_people_groups = 0
over_foutry_one_people_groups = 0
total_people = 0
total_musala = 0
total_monblan = 0
total_kilimandjaro = 0
total_ktwo = 0
total_everest = 0

for groups in range(0, number_groups):
    group = int(input())
    total_people += group
    if group <= 5:
        five_people_gorups += 1
        total_musala += group
    elif 5 < group <= 12:
        six_to_twelve_groups += 1
        total_monblan += group
    elif 12 < group <= 25:
        thirteen_people_gorups += 1
        total_kilimandjaro += group
    elif 25 < group <= 40:
        twenty_six_people_groups += 1
        total_ktwo += group
    elif group > 40:
        over_foutry_one_people_groups += 1
        total_everest += group

musala = total_musala / total_people * 100
monblan = total_monblan / total_people * 100
kilimandjaro = total_kilimandjaro / total_people * 100
ktwo = total_ktwo / total_people * 100
everest = total_everest / total_people * 100

print(f"{musala:.2f}%\n{monblan:.2f}%\n{kilimandjaro:.2f}%\n{ktwo:.2f}%\n{everest:.2f}%")
