import re

initial_string = input()
pattern = r'([=/])(?P<place>[A-Z]{1}[a-zA-Z]{2,})\1'
found_destinations = [match.group('place') for match in re.finditer(pattern, initial_string)]

print(f'Destinations: {", ".join(found_destinations)}')
print(f'Travel Points: {sum(len(x) for x in found_destinations)}')




# import re
#
# initial_string = input()
#
# pattern = r'([=/])(?P<place>[A-Z]{1}[a-zA-Z]{2,})\1'
#
# found_destinations = []
# for match in re.finditer(pattern, initial_string):
#     found_destinations.append(match.group('place'))
#
# print(f'Destinations: {", ".join(found_destinations)}')
# print(f'Travel Points: {sum(len(x) for x in found_destinations)}')
