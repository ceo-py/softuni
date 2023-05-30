number_claiming_groups = int(input())

musala = 0
monblan = 0
klimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(number_claiming_groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        klimanjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

percent_musala = musala / total_people * 100
percent_monblan = monblan / total_people * 100
percent_klimanjaro = klimanjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_klimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")







# group_count = int(input())
# musala =  0
# monblan =  0
# kilimandjaro =  0
# ktwo =  0
# everest = 0
#
# all_groups = 0
#
# for grups in range(1, group_count + 1):
#     grups_people = int(input())
#
#     if grups_people <= 5:
#         musala += grups_people
#     elif (grups_people >= 6) and (grups_people <= 12):
#         monblan += grups_people
#     elif (grups_people >= 13) and (grups_people <= 25):
#         kilimandjaro += grups_people
#     elif (grups_people >= 26) and (grups_people <= 40):
#         ktwo += grups_people
#     elif grups_people >= 41:
#         everest += grups_people
#     all_groups += grups_people
#
# print("%.2f" % (musala / all_groups * 100) + "%")
# print("%.2f" % (monblan / all_groups * 100) + "%")
# print("%.2f" % (kilimandjaro / all_groups * 100) + "%")
# print("%.2f" % (ktwo / all_groups * 100) + "%")
# print("%.2f" % (everest / all_groups * 100) + "%")
#
#
#



#
# group_count = int(input())
# groups_mountains = {
#     "musala" : 0,
#     "monblan": 0,
#     "kilimandjaro": 0,
#     "ktwo": 0,
#     "everest": 0
# }
# all_groups = 0
#
# for grups in range(1, group_count + 1):
#     grups_people = int(input())
#
#     if grups_people <= 5:
#         groups_mountains["musala"] += grups_people
#
#     elif ((grups_people >= 6) and (grups_people <= 12)):
#         groups_mountains["monblan"] += grups_people
#     elif ((grups_people >= 13) and (grups_people <= 25)):
#
#         groups_mountains["kilimandjaro"] += grups_people
#     elif ((grups_people >= 26) and (grups_people <= 40)):
#
#         groups_mountains["ktwo"] += grups_people
#     elif grups_people >= 41:
#
#         groups_mountains["everest"] += grups_people
#     all_groups += grups_people
#
#
# print("%.2f" % (groups_mountains["musala"] / all_groups * 100) + "%")
# print("%.2f" % (groups_mountains["monblan"] / all_groups * 100)+ "%")
# print("%.2f" % (groups_mountains["kilimandjaro"] / all_groups * 100)+ "%")
# print("%.2f" % (groups_mountains["ktwo"] / all_groups * 100)+ "%")
# print("%.2f" % (groups_mountains["everest"] / all_groups * 100)+ "%")
