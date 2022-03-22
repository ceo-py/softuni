import re

demons = re.split(", *", input())
demon_book = {}

demon_health_pattern = r'[^\d\+\-*\/\.]'
demon_damage_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demon_operators_pattern = r'[*\/]'

for demon in demons:
    demon = demon.strip()
    demon_health = re.findall(demon_health_pattern, demon)
    demon_book[demon] = []
    demon_book[demon].append(sum(ord(match) for match in demon_health))

    demon_damage = re.finditer(demon_damage_pattern, demon)
    operators = re.findall(demon_operators_pattern, demon)
    current_demon_damage = 0

    for value in demon_damage:
        current_demon_damage += float(value.group(0))

    for operator in operators:
        if operator == '*':
            current_demon_damage *= 2
        elif operator == '/':
            current_demon_damage /= 2

    demon_book[demon].append(current_demon_damage)

for demon, qualities in sorted(demon_book.items()):
    print(f'{demon} - {qualities[0]} health, {qualities[1]:.2f} damage')
