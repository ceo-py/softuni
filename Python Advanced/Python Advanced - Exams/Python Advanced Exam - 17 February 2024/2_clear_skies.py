matrix_size = int(input())
matrix = []
movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
jet_fighter = {
    'armor': 300,
    'position': [0, 0],
    'enemies': 0
}

for row in range(matrix_size):
    matrix.append(list(input()))
    if 'J' in matrix[row]:
        index_of_jet = matrix[row].index('J')
        jet_fighter['position'] = [row, index_of_jet]
        matrix[row][index_of_jet] = '-'
    jet_fighter['enemies'] += matrix[row].count('E')

while jet_fighter['armor'] > 0:
    command = input()

    jet_fighter['position'] = [movements[command][0] + \
        jet_fighter['position'][0], movements[command][1] + \
        jet_fighter['position'][1]]
    step_on = matrix[jet_fighter['position'][0]][jet_fighter['position'][1]]

    if step_on == '-':
        continue

    if step_on == 'R':
        jet_fighter['armor'] = 300
        matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = '-'
        continue

    if step_on == 'E':
        jet_fighter['enemies'] -= 1
        matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = '-'

    if jet_fighter['enemies'] == 0:
        print('Mission accomplished, you neutralized the aerial threat!')
        matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = 'J'
        break

    jet_fighter['armor'] -= 100

else:
    matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = 'J'
    print(
        f"Mission failed, your jetfighter was shot down! Last coordinates {jet_fighter['position']}!")
[print(*row, sep='') for row in matrix]



'''
input

5
-R---
-J--E
-E---
--E-E
-R---
up
down
down
down
right
right
right
'''

'''
output
Mission failed, your jetfighter was shot down! Last coordinates [3, 4]!
-----
----E
-----
----J
-R---
'''
