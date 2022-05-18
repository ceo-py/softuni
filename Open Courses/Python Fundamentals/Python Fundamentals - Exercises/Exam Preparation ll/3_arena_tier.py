data_input = input()

gladiator_info = {}
result_list = []


def vs_duel(glad_name_one, glad_name_two):
    if all([glad_name_one in gladiator_info, glad_name_two in gladiator_info]):
        for skills in gladiator_info[glad_name_one]:
            if all([skills in gladiator_info[glad_name_two], skills != "total"]):
                if gladiator_info[glad_name_one]["total"] > gladiator_info[glad_name_two]["total"]:
                    del gladiator_info[glad_name_two]
                elif gladiator_info[glad_name_one]["total"] < gladiator_info[glad_name_two]["total"]:
                    del gladiator_info[glad_name_one]
                break


def adding_gladiator(glad_name, skill, points):
    if glad_name not in gladiator_info:
        gladiator_info[glad_name] = {}
    if skill not in gladiator_info[glad_name]:
        gladiator_info[glad_name][skill] = 0
    if points > gladiator_info[glad_name][skill]:
        gladiator_info[glad_name][skill] = points
    gladiator_info[glad_name]["total"] = 0
    gladiator_info[glad_name]["total"] = sum(gladiator_info[glad_name].values())


while data_input != "Ave Cesar":
    glad_name, *other = data_input.split()
    if "vs" in other[0]:
        vs_duel(glad_name, other[-1])
    else:
        _, skill, _,  points = other
        adding_gladiator(glad_name, skill, int(points))
    data_input = input()


def show_result():
    for name in gladiator_info:
        result_list.append({"name": name, "total": gladiator_info[name]["total"]})
    for show in sorted(result_list, key=lambda x: (-x["total"], x["name"])):
        print(f"{show['name']}: {show['total']} skill")
        for skills, points in sorted(gladiator_info[show['name']].items(), key=lambda x: (-x[1], x[0])):
            if skills != "total":
                print(f"- {skills} <!> {points}")


show_result()

