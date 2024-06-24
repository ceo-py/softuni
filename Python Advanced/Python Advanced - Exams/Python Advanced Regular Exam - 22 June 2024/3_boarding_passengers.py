def boarding_passengers(capacity_ship, *args):
    passengers = {}
    output = ['Boarding details by benefit plan:']
    boarding_msg = 'All passengers are successfully boarded!' if capacity_ship == sum(
        x for x, _ in args) else f'Boarding unsuccessful. Cruise ship at full capacity.'

    for number_of_passengers, program_name in args:
        if capacity_ship - number_of_passengers < 0:
            continue

        capacity_ship -= number_of_passengers
        passengers[program_name] = passengers.get(
            program_name, 0) + number_of_passengers

    [output.append(f"## {key}: {value} guests") for key, value in sorted(
        passengers.items(), key=lambda item: (-item[1], item[0]))]

    if capacity_ship > 0:
        output.append(
            f'Partial boarding completed. Available capacity: {capacity_ship}.')
    else:
        output.append(boarding_msg)

    return '\n'.join(output)


# print(boarding_passengers(150, (35, 'Diamond'),
#       (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

'''
Boarding details by benefit plan:
## Platinum: 55 guests
## Diamond: 35 guests
## Gold: 35 guests
## First Cruiser: 25 guests
All passengers are successfully boarded!
'''

# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'),
#                           (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))

'''
Boarding details by benefit plan:
## Diamond: 35 guests
## First Cruiser: 25 guests
## Gold: 25 guests
## Platinum: 15 guests
Boarding unsuccessful. Cruise ship at full capacity.
'''
# print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'),
#       (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
