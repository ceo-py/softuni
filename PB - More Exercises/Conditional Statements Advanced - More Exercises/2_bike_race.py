cyclists_juniors = int(input())
cyclists_seniors = int(input())
route_type = input()

tournament_info = {
    "juniors": {
        "trail": 5.50,
        "cross-country": 8,
        "downhill": 12.25,
        "road": 20,
        "tax": 0.05,
        "off": 0.25},
    "seniors": {
        "trail": 7,
        "cross-country": 9.50,
        "downhill": 13.75,
        "road": 21.50}

}
total_cyclists = cyclists_juniors + cyclists_seniors

if route_type == "cross-country" and total_cyclists >= 50:
    junior_total = (tournament_info["juniors"][route_type] - (tournament_info["juniors"][route_type]) \
                   * tournament_info["juniors"]["off"]) * cyclists_juniors
    seniors_total = (tournament_info["seniors"][route_type] - (tournament_info["seniors"][route_type]) \
                    * tournament_info["juniors"]["off"]) * cyclists_seniors
    total = junior_total + seniors_total
    total += - (total * tournament_info["juniors"]["tax"])
else:
    junior_total = tournament_info["juniors"][route_type] * cyclists_juniors
    seniors_total = tournament_info["seniors"][route_type] * cyclists_seniors
    total = junior_total + seniors_total
    total += - (total * tournament_info["juniors"]["tax"])

print(f"{total:.2f}")
