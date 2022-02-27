number_visitors_in_gym = int(input())

gym_info = {
    "Back": 0,
    "Chest": 0,
    "Legs": 0,
    "Abs": 0,
    "Protein shake": 0,
    "Protein bar": 0
}

for i in range(1, number_visitors_in_gym + 1):
    activities_in_gym = input()

    gym_info[activities_in_gym] += 1

work_out = gym_info["Back"] + gym_info["Chest"] + gym_info["Legs"] + gym_info["Abs"]
protein = gym_info["Protein shake"] + gym_info["Protein bar"]

work_out = (work_out / number_visitors_in_gym) * 100
protein = (protein / number_visitors_in_gym) * 100

for type_work_out, number in gym_info.items():
    print(f"{number} - {type_work_out.lower()}")

print(f"{work_out:.2f}% - work out")
print(f"{protein:.2f}% - protein")
