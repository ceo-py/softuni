competitions_type = input()
ticket_type = input()
number_tickets = int(input())
picture_with_trophy = input()

tournament_info = {
    "Quarter final": {
        "Standard": 55.50,
        "Premium": 105.20,
        "VIP": 118.90},
    "Semi final": {
        "Standard": 75.88,
        "Premium": 125.22,
        "VIP": 300.40},
    "Final": {
        "Standard": 110.10,
        "Premium": 160.66,
        "VIP": 400},
}

total = tournament_info[competitions_type][ticket_type] * number_tickets

if total > 4000 and picture_with_trophy == "Y":
    total = (total - (total * 0.25))

elif total > 2500 and picture_with_trophy == "Y":
    total = total - (total * 0.10) + (40 * number_tickets)

elif total > 4000 and picture_with_trophy == "N":
    total = (total - (total * 0.25))

elif total > 2500 and picture_with_trophy == "N":
    total = (total - (total * 0.10))

elif total <= 2500 and picture_with_trophy == "Y":
    total += 40 * number_tickets


print(f"{total:.2f}")
