command_input = input()

player_info = {}
best_players = []


def duel_players(name_one, name_two):
    if (name_one and name_two) in player_info:
        for p_one in player_info[name_one]:
            if p_one in player_info[name_two]:
                total_pl_one = sum(player_info[name_one].values())
                total_pl_two = sum(player_info[name_two].values())
                if total_pl_one > total_pl_two:
                    del player_info[name_two]
                elif total_pl_one < total_pl_two:
                    del player_info[name_one]
                break


def adding_players_roles(player, position, skill):
    if player not in player_info:
        player_info[player] = {}
    if position not in player_info[player]:
        player_info[player][position] = 0
    if player_info[player][position] < skill:
        player_info[player][position] = skill


while command_input != "Season end":
    if " vs " in command_input:
        command_input = command_input.split(" vs ")
        duel_players(command_input[0], command_input[-1])
    else:
        command_input = command_input.split(" -> ")
        adding_players_roles(command_input[0], command_input[1], int(command_input[-1]))
    command_input = input()


def show_result():
    for p_name in player_info:
        best_players.append({"name": p_name, "total_score": sum(player_info[p_name].values())})
    for show in sorted(best_players, key=lambda item: (-item["total_score"], item["name"])):
        print(f"{show['name']}: {show['total_score']} skill")
        for pos, skill in sorted(player_info[show['name']].items(), key=lambda item: (-item[1], item[0])):
            print(f"- {pos} <::> {skill}")


show_result()
