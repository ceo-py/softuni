import math

shells = {}

town_information = input()

while town_information != "Aggregate":
    town_information = town_information.split()
    if town_information[0] not in shells:
        shells[town_information[0]] = []
    if town_information[-1] not in shells[town_information[0]]:
        shells[town_information[0]].append(town_information[-1])
    town_information = input()


def show_result():
    for town in shells:
        sum_shells = [int(x) for x in shells[town]]
        diff = sum(sum_shells) - (sum(sum_shells) / len(sum_shells))
        print(f"{town} -> {', '.join(shells[town])} ({math.ceil(diff)})")


show_result()
