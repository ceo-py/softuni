import re

decrypt_key = input()

team_info = {}
escape_characters = ["[", "]", "(", ")", "{", "}", "*", "+", "?", "|", ".", "\\"]
key_ = ""
for x in decrypt_key:
    if x in escape_characters:
        key_ += f"\{x}"
    else:
        key_ += f"{x}"

decrypt_msg = input()
pattern = re.compile(f"({key_})(.*)({key_}).*({key_})(.*)({key_})")
score_pattern = re.compile(r"\d+:\d+")
while decrypt_msg != "final":
    matches = pattern.findall(decrypt_msg)
    for show in matches:
        home_team, away_team = show[1][::-1].upper(), show[4][::-1].upper()
        home_team_score, away_team_score = score_pattern.findall(decrypt_msg)[0].split(":")
        if home_team not in team_info:
            team_info[home_team] = {"points": 0, "goals": 0}
        if away_team not in team_info:
            team_info[away_team] = {"points": 0, "goals": 0}
        if home_team_score > away_team_score:
            team_info[home_team]["points"] += 3
        elif home_team_score < away_team_score:
            team_info[away_team]["points"] += 3
        else:
            team_info[away_team]["points"] += 1
            team_info[home_team]["points"] += 1
        team_info[home_team]["goals"] += int(home_team_score)
        team_info[away_team]["goals"] += int(away_team_score)
    decrypt_msg = input()

result_list = []


def show_result():
    for name in team_info:
        result_list.append({"team name": name, "points": team_info[name]["points"], "goals": team_info[name]["goals"]})
    print("League standings:")
    for pos, show in enumerate(sorted(result_list, key=lambda item: (-item["points"], item["team name"])), 1):
        print(f"{pos}. {show['team name']} {show['points']}")
    print("Top 3 scored goals:")
    for pos, show in enumerate(sorted(result_list, key=lambda item: (-item["goals"], item["team name"])), 1):
        print(f"- {show['team name']} -> {show['goals']}")
        if pos == 3:
            break


show_result()
