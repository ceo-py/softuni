command = input()

moba_possition_info = {}
result = {}
skills_p1 = list()
skills_p2 = list()
duel_result = list()


def add_player(name, spec, points):
    if name not in moba_possition_info:
        moba_possition_info[name] = {}
        moba_possition_info[name] = {}
    if spec not in moba_possition_info[name]:
        moba_possition_info[name][spec] = points
    if moba_possition_info[name][spec] < points:
        moba_possition_info[name][spec] = points


def duel_player(player_one, player_two):
    check_status = False
    if (player_one and player_two) in moba_possition_info:
        p1 = len(moba_possition_info[player_one])
        p2 = len(moba_possition_info[player_two])
        if p1 >= p2:
            for key in moba_possition_info[player_one]:
                if key in moba_possition_info[player_two]:
                    spec = key
                    check_status = True
                    break
        else:
            for key in moba_possition_info[player_two]:
                if key in moba_possition_info[player_one]:
                    spec = key
                    check_status = True
                    break
        if check_status:
            total_score_players()
            if result[player_one] > result[player_two]:
                del moba_possition_info[player_two][spec]
                del result[player_two]
            elif result[player_two] > result[player_one]:
                del moba_possition_info[player_one][spec]
                del result[player_one]

def total_score_players():
    for name in moba_possition_info:
        total = moba_possition_info[name].values()
        result[name] = sum(total)

def show_result():

    total_score_players()
    resultt = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # resultt = sorted(resultt, key=lambda x: x[0], reverse=True)
    for name in resultt:
        if name[1] > 0:
            print(f"{name[0]}: {name[1]} skill")
            name_sort = sorted(moba_possition_info[name[0]].items(), key=lambda x: x[1], reverse=True)
            for info in name_sort:
                print(f"- {info[0]} <::> {info[1]}")

while command != "Season end":
    if "vs" in command:
        command = command.split(" vs ")
        name_p1 = command[0]
        name_p2 = command[-1]
        duel_player(name_p1, name_p2)
    else:
        command = command.split(" -> ")
        name = command[0]
        spec = command[1]
        points = int(command[-1])
        add_player(name, spec, points)

    command = input()

total_score_players()
show_result()
