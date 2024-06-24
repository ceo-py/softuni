from typing import Tuple

square_matrix_size = int(input())
matrix = []

movement_directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

bee_details = {
    'position': {
        'row': 0,
        'col': 0
    },
    'energy': {
        'amount': 15,
        'restored': False
    },
    'collected nectar': 0,

}

for row in range(square_matrix_size):
    matrix.append(list(input()))
    if 'B' in matrix[row]:
        col = matrix[row].index('B')
        bee_details['position']['row'], bee_details['position']['col'] = (
            row, col)
        matrix[row][col] = '-'


def traverse_bee(row: int, col: int) -> Tuple[int, int]:
    bee_details['position']['row'] += row
    bee_details['position']['col'] += col
    if bee_details['position']['row'] < 0:
        bee_details['position']['row'] = square_matrix_size - 1

    elif bee_details['position']['row'] >= square_matrix_size:
        bee_details['position']['row'] = 0

    if bee_details['position']['col'] < 0:
        bee_details['position']['col'] = square_matrix_size - 1

    elif bee_details['position']['col'] >= square_matrix_size:
        bee_details['position']['col'] = 0


while bee_details['energy']['amount'] > 0:
    direction = input()
    traverse_bee(*movement_directions[direction])
    step_on = matrix[bee_details['position']
    ['row']][bee_details['position']['col']]
    bee_details['energy']['amount'] -= 1

    if step_on.isdigit():
        bee_details['collected nectar'] += int(step_on)
        matrix[bee_details['position']
        ['row']][bee_details['position']['col']] = '-'

    elif step_on == 'H':
        print(
            f"Beesy did not manage to collect enough nectar." if not bee_details['collected nectar'] >= 30 else
            f"Great job, Beesy! The hive is full. Energy left: {bee_details['energy']['amount']}")
        break

    elif bee_details['energy']['amount'] == 0 and not bee_details['energy']['restored'] and bee_details[
        'collected nectar'] >= 30:
        bee_details['energy']['restored'] = True
        restore_energy_amount = bee_details['collected nectar'] - 30
        bee_details['collected nectar'] = 30
        bee_details['energy']['amount'] = restore_energy_amount
else:
    print('This is the end! Beesy ran out of energy.')

matrix[bee_details['position']
['row']][bee_details['position']['col']] = 'B'
[print(''.join(row)) for row in matrix]

'''
5
--B--
H-987
-4812
5----
2----
down
right
right
down
left
left
left
down
left
up
up
up

'''
