matrix_size = int(input())
matrix = []
traveller = {
    'health': 100,
    'pos': (0, 0),
}
movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for row in range(matrix_size):
    matrix.append(list(input()))
    if 'P' in matrix[row]:
        col = matrix[row].index('P')
        traveller['pos'] = (row, col)
        matrix[row][col] = '-'

while True:
    next_step = input()

    traveller['pos'] = traveller['pos'][0] + \
        movements[next_step][0], traveller['pos'][1] + movements[next_step][1]

    try:
        step_on = matrix[traveller['pos'][0]][traveller['pos'][1]]

        if step_on == 'X':
            print('Player escaped the maze. Danger passed!')
            break

        if step_on == 'M':
            traveller['health'] -= 40

            if traveller['health'] <= 0:
                print('Player is dead. Maze over!')
                traveller['health'] = 0
                break

        if step_on == 'H':
            traveller['health'] += 15

            if traveller['health'] > 100:
                traveller['health'] = 100

        matrix[traveller['pos'][0]][traveller['pos'][1]] = '-'

    except IndexError:
        traveller['pos'] = traveller['pos'][0] - \
            movements[next_step][0], traveller['pos'][1] - \
            movements[next_step][1]

matrix[traveller['pos'][0]][traveller['pos'][1]] = 'P'
print(f"Player's health: {traveller['health']} units")
[print(''.join(row)) for row in matrix]



# matrix_size = int(input())
# matrix = []
# traveller = {
#     'health': 100,
#     'pos': (0, 0),
# }
# monsters = 0
# movements = {
#     'down': (1, 0),
#     'right': (0, 1),
#     'left': (0, -1),
#     'up': (-1, 0),
# }
#
# for row in range(matrix_size):
#     matrix.append(list(input()))
#     if 'M' in matrix[row]:
#         monsters += 1
#     if 'P' in matrix[row]:
#         col = matrix[row].index('P')
#         traveller['pos'] = (row, col)
#         matrix[row][col] = '-'
#
# while True:
#     next_move = input()
#
#     traveller['pos'] = traveller['pos'][0] + movements[next_move][0], traveller['pos'][1] + movements[next_move][1]
#
#     try:
#         step_on = matrix[traveller['pos'][0]][traveller['pos'][1]]
#         if step_on == 'X':
#             print('Player escaped the maze. Danger passed!')
#             break
#
#         if step_on == 'H':
#             traveller['health'] += 15
#             if traveller['health'] > 100:
#                 traveller['health'] = 100
#
#         elif step_on == 'M':
#             monsters -= 1
#             traveller['health'] -= 40
#
#             if traveller['health'] <= 0:
#                 traveller['health'] = 0
#                 print('Player is dead. Maze over!')
#                 break
#
#         matrix[traveller['pos'][0]][traveller['pos'][1]] = '-'
#
#     except IndexError:
#         traveller['pos'] = traveller['pos'][0] - movements[next_move][0], traveller['pos'][1] - movements[next_move][1]
#         continue
#
# matrix[traveller['pos'][0]][traveller['pos'][1]] = 'P'
# print(f"Player's health: {traveller['health']} units")
# [print(*row, sep='') for row in matrix]

'''
input
5
-----
-PM--
-M---
---H-
-X---
down
right
down
down
left
'''

'''
output

On the first line:
If the traveller has less than or equal to 0 health:
"Player is dead. Maze over!"
If the traveller survived with more than 0 health and managed to escape the maze: 
"Player escaped the maze. Danger passed!"
On the second line, print the final value of the traveller's health following the format:
"Player's health: {health value} units"
On the next lines, print the final state of the matrix with the traveller in its ending position. Each row - on a new line.
'''
