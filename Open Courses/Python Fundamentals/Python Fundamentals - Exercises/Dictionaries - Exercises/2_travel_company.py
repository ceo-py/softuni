adding_city = input()

transport_info = {}

while adding_city != "ready":
    adding_city = adding_city.split(":")
    if adding_city[0] not in transport_info:
        transport_info[adding_city[0]] = {}
    additional_info = adding_city[1].split(",")
    for transport in additional_info:
        type_info = transport.split("-")
        if type_info[0] not in transport_info[adding_city[0]]:
            transport_info[adding_city[0]][type_info[0]] = 0
        transport_info[adding_city[0]][type_info[0]] = int(type_info[-1])
    adding_city = input()

travel_time = input()

while travel_time != "travel time!":
    travel_time = travel_time.split()
    if int(travel_time[-1]) <= sum(transport_info[travel_time[0]].values()):
        print(f"{travel_time[0]} -> all {travel_time[-1]} accommodated")
    else:
        print(
            f"{travel_time[0]} -> all except {int(travel_time[-1]) - sum(transport_info[travel_time[0]].values())} accommodated")
    travel_time = input()
