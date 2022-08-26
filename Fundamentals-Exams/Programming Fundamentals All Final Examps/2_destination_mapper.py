import re

main_string = input()

pattern = re.compile(r"([=/])(?P<location>[A-Z][a-zA-Z]{2,})\1")

list_result = []
result = re.finditer(pattern, main_string)
total_travel_points = 0
for show in result:
    total_travel_points += len(show["location"])
    list_result.append(show["location"])

print(f"Destinations: {', '.join(list_result)}")
print(f"Travel Points: {total_travel_points}")