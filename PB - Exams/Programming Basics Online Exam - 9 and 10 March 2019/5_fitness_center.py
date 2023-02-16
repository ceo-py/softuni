jym_visitors = int(input())

training_people = 0
products = 0

back = 0
chest = 0
legs = 0
abs_ = 0
shake = 0
bar = 0

for person in range(jym_visitors):
    activity = input()

    if "Protein shake" == activity or "Protein bar" == activity:
        products += 1
    else:
        training_people += 1

    if activity == "Back":
        back += 1

    elif activity == "Chest":
        chest += 1

    elif activity == "Legs":
        legs += 1

    elif activity == "Abs":
        abs_ += 1

    elif activity == "Protein shake":
        shake += 1

    elif activity == "Protein bar":
        bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{(training_people / jym_visitors) * 100:.2f}% - work out")
print(f"{(products / jym_visitors) * 100:.2f}% - protein")







#
#
#
# number_visitors_in_gym = int(input())
#
# gym_info = {
#     "Back": 0,
#     "Chest": 0,
#     "Legs": 0,
#     "Abs": 0,
#     "Protein shake": 0,
#     "Protein bar": 0
# }
#
# for i in range(1, number_visitors_in_gym + 1):
#     activities_in_gym = input()
#
#     gym_info[activities_in_gym] += 1
#
# work_out = gym_info["Back"] + gym_info["Chest"] + gym_info["Legs"] + gym_info["Abs"]
# protein = gym_info["Protein shake"] + gym_info["Protein bar"]
#
# work_out = (work_out / number_visitors_in_gym) * 100
# protein = (protein / number_visitors_in_gym) * 100
#
# for type_work_out, number in gym_info.items():
#     print(f"{number} - {type_work_out.lower()}")
#
# print(f"{work_out:.2f}% - work out")
# print(f"{protein:.2f}% - protein")
