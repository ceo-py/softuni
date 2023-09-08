cyclists_juniors = int(input())
cyclists_seniors = int(input())
route_type = input()

juniors_tax = 0
seniors_tax = 0

if route_type == 'trail':
    juniors_tax = 5.50
    seniors_tax = 7

elif route_type == 'cross-country':
    juniors_tax = 8
    seniors_tax = 9.50

    if cyclists_juniors + cyclists_seniors >= 50:
        juniors_tax *= 0.75
        seniors_tax *= 0.75

elif route_type == 'downhill':
    juniors_tax = 12.25
    seniors_tax = 13.75

elif route_type == 'road':
    juniors_tax = 20
    seniors_tax = 21.50

total_sum = ((cyclists_juniors * juniors_tax) + (cyclists_seniors * seniors_tax)) * 0.95
print(f'{total_sum:.2f}')







# cyclists_juniors = int(input())
# cyclists_seniors = int(input())
# route_type = input()
#
# tournament_info = {
#     "juniors": {
#         "trail": 5.50,
#         "cross-country": 8,
#         "downhill": 12.25,
#         "road": 20,
#         "tax": 0.05,
#         "off": 0.25},
#     "seniors": {
#         "trail": 7,
#         "cross-country": 9.50,
#         "downhill": 13.75,
#         "road": 21.50}
#
# }
# total_cyclists = cyclists_juniors + cyclists_seniors
#
# if route_type == "cross-country" and total_cyclists >= 50:
#     junior_total = (tournament_info["juniors"][route_type] - (tournament_info["juniors"][route_type]) \
#                    * tournament_info["juniors"]["off"]) * cyclists_juniors
#     seniors_total = (tournament_info["seniors"][route_type] - (tournament_info["seniors"][route_type]) \
#                     * tournament_info["juniors"]["off"]) * cyclists_seniors
#     total = junior_total + seniors_total
#     total += - (total * tournament_info["juniors"]["tax"])
# else:
#     junior_total = tournament_info["juniors"][route_type] * cyclists_juniors
#     seniors_total = tournament_info["seniors"][route_type] * cyclists_seniors
#     total = junior_total + seniors_total
#     total += - (total * tournament_info["juniors"]["tax"])
#
# print(f"{total:.2f}")
