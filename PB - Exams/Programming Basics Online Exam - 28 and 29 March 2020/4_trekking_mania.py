group_count = int(input())
groups_mountains = {
    "musala" : 0,
    "monblan": 0,
    "kilimandjaro": 0,
    "ktwo": 0,
    "everest": 0
}
all_groups = 0

for grups in range(1, group_count + 1):
    grups_people = int(input())

    if grups_people <= 5:
        groups_mountains["musala"] += grups_people

    elif ((grups_people >= 6) and (grups_people <= 12)):
        groups_mountains["monblan"] += grups_people
    elif ((grups_people >= 13) and (grups_people <= 25)):

        groups_mountains["kilimandjaro"] += grups_people
    elif ((grups_people >= 26) and (grups_people <= 40)):

        groups_mountains["ktwo"] += grups_people
    elif grups_people >= 41:

        groups_mountains["everest"] += grups_people
    all_groups += grups_people


print("%.2f" % (groups_mountains["musala"] / all_groups * 100) + "%")
print("%.2f" % (groups_mountains["monblan"] / all_groups * 100)+ "%")
print("%.2f" % (groups_mountains["kilimandjaro"] / all_groups * 100)+ "%")
print("%.2f" % (groups_mountains["ktwo"] / all_groups * 100)+ "%")
print("%.2f" % (groups_mountains["everest"] / all_groups * 100)+ "%")
