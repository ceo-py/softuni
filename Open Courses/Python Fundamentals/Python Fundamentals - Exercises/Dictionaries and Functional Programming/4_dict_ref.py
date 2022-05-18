dic_ref = {}

names_given = input()

while names_given != "end":
    names_given = names_given.split(" = ")
    if names_given[-1].isdigit():
        dic_ref[names_given[0]] = int(names_given[-1])

    elif names_given[-1] in dic_ref:
        dic_ref[names_given[0]] = dic_ref[names_given[-1]]
    names_given = input()

for key, value in dic_ref.items():
    print(f"{key} === {value}")