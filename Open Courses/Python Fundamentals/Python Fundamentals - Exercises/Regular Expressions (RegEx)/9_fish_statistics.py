import re

fish_info = input()
fish_dic = {"type": {"x": "Dead", "-": "Asleep", "'": "Awake"}, "fishes": {}}
pattern = re.compile(f"((<|>)+)((\()+)(x|-|')>")
matches = pattern.finditer(fish_info)
for pos, show in enumerate(matches, 1):
    tail, body, status = show[1].count(">"), show[3].count("("), show[5]
    if tail > 5:
        type_tail = "Long"
    elif tail > 1:
        type_tail = "Medium"
    elif tail == 1:
        type_tail = "Short"
    else:
        tail = ""
        type_tail = "None"
    if type_tail != "None":
        tail = f" ({tail * 2} cm)"
    if body > 10:
        type_body = "Long"
    elif body > 5:
        type_body = "Medium"
    else:
        type_body = "Short"
    fish_dic["fishes"][pos] = {}
    fish_dic["fishes"][pos][f"Fish {pos}"] = show[0]
    fish_dic["fishes"][pos]["  Tail type"] = f"{type_tail}{tail}"
    fish_dic["fishes"][pos]["  Body type"] = f"{type_body} ({body * 2} cm)"
    fish_dic["fishes"][pos]["  Status"] = fish_dic["type"][status]


def show_results():
    for num in fish_dic["fishes"]:
        for key, value in fish_dic["fishes"][num].items():
            print(f"{key}: {value}")


if fish_dic["fishes"]:
    show_results()
else:
    print("No fish found.")
