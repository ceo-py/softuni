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




# pool = {}
#
# command = input()
# while command != 'Season end':
#     if "->" in command:
#         name, skill, points = [int(i) if i.isdigit() else i for i in command.split(" -> ")]
#         if name not in pool:
#             pool[name] = {skill: points}
#         elif name in pool and skill not in pool[name]:
#             pool[name][skill] = points
#         elif name in pool and skill in pool[name]:
#             if pool[name][skill] < points:
#                 pool[name][skill] = points
#
#     else:
#         player1, player2 = command.split(" vs ")
#         if player1 in pool and player2 in pool:
#             for position, points in pool[player1].items():
#                 if position in pool[player2].keys():
#                     if points < pool[player2][position]:
#                         del pool[player1]
#                     elif pool[player2][position] < pool[player1][position]:
#                         del pool[player2]
#                     break
#
#
#     command = input()
#
# # total points generating and sorting
# total_points = {}
# for name in pool.keys():
#     for v in pool[name].values():
#         if name not in total_points:
#             total_points[name] = 0
#         total_points[name] += v
# total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
#
# # inside points sorting
# for name in pool.keys():
#     for k, v in pool[name].items():
#         pool[name] = dict(sorted(pool[name].items(), key=lambda x: (-x[1], x[0])))
#
# for name, totalpoints in total_points.items():
#     print(f"{name}: {totalpoints} skill")
#     for k, v in pool[name].items():
#         print(f"- {k} <::> {v}")