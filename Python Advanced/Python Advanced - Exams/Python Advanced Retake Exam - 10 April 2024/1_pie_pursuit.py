from collections import deque


contestants = [int(x) for x in input().split()]
pies = deque(int(x) for x in input().split())

while contestants and pies:
    contestant = contestants.pop()
    pie = pies.popleft()

    difference = abs(contestant - pie)

    if contestant >= pie:
        if difference > 0:
            contestants.append(difference)
        continue

    if len(pies) == 0:
        pies.append(difference)
        continue

    if difference == 1:
        pies[0] += difference
        continue

    pies.appendleft(difference)

if not pies and contestants:
    print('We will have to wait for more pies to be baked!')
    print(f'Contestants left: {", ".join(str(x) for x in contestants)}')

elif not pies and not contestants:
    print('We have a champion!')

elif pies and not contestants:
    print('Our contestants need to rest!')
    print(f'Pies left: {", ".join(str(x) for x in pies)}')



# 5 8 4 6
# 3 7 2 9



# from collections import deque
#
# contestants = [int(x) for x in input().split()]
# pies = deque(int(x) for x in input().split())
#
# while contestants and pies:
#     current_contestant = contestants.pop()
#     current_pie = pies.popleft()
#
#     difference = abs(current_contestant - current_pie)
#
#     if current_contestant >= current_pie:
#
#         if difference > 0:
#             contestants.append(difference)
#
#     elif current_pie > current_contestant:
#         if len(pies) == 0:
#             pies.append(difference)
#             continue
#
#         if difference == 1:
#             pies[0] += difference
#             continue
#
#         pies.appendleft(difference)
#
# if not contestants and not pies:
#     print("We have a champion!")
#
# elif not pies and contestants:
#     print("We will have to wait for more pies to be baked!")
#     print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
#
# elif pies and not contestants:
#     print("Our contestants need to rest!")
#     print(f"Pies left: {', '.join(str(x) for x in pies)}")

'''
input

5 8 4 6
3 7 2 9
'''


'''
output
If the pies are over, and there are contestants left: 
"We will have to wait for more pies to be baked!"
The final state of the contestants' sequence: 
"Contestants left: {contestant1}, {contestant2}, … {contestantn}"
If both the pies and contestants are over: 
"We have a champion!"
If the contestants are over, but there are pies left: 
"Our contestants need to rest!"
The final state of the pie sequence
"Pies left: {pie1}, {pie2}, … {pien}"
'''
