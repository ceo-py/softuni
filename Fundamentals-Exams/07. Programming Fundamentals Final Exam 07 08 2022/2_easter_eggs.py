import re

initial_string = input()

pattern = r"[@#](?P<color>[a-z]{3,})[@#]([^a-zA-Z0-9]*)/(?P<amount>[0-9]+)/"

for match in re.finditer(pattern, initial_string):
    print(f"You found {match.group('amount')} {match.group('color')} eggs!")
