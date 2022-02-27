command = input()

standings = {}
as_list = []
total_score = {}


def add_people(name, algo, points):
    if algo not in standings:
        standings[algo] = {}
    if name not in standings[algo]:
        standings[algo][name] = 0
    # if standings[algo][name] == points:
    #     standings[algo][name] += points
    if standings[algo][name] < points:
        standings[algo][name] = points
    else:
        standings[algo][name] = points


def print_position(individual):
    if individual:
        separator = "->"
    else:
        separator = "<::>"
    name = "name"
    points = "points"
    possition = 1
    for pos in as_list:
        print(f"{possition}. {pos[name]} {separator} {pos[points]}")
        possition += 1


def show_results():
    for name_algo in standings:
        total = 0

        for name, points in standings[name_algo].items():
            total += 1
            individual_standings = {"name": name, "points": points}
            if name not in total_score:
                total_score[name] = points
            else:
                total_score[name] += points
            as_list.append(individual_standings)

        print(f"{name_algo}: {total} participants")
        as_list.sort(key=lambda item: (-item['points'], item['name']))
        print_position(False)
        as_list.clear()
    # total result
    for name_t, score_t in total_score.items():
        individual_standings = {"name": name_t, "points": score_t}
        as_list.append(individual_standings)
    as_list.sort(key=lambda item: (-item['points'], item['name']))
    print("Individual standings:")
    print_position(True)


while command != "no more time":
    command = command.split(" -> ")
    name = command[0]
    algo = command[1]
    points = int(command[-1])
    add_people(name, algo, points)
    command = input()

show_results()
