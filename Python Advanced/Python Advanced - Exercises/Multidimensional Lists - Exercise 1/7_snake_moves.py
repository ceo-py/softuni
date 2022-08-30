from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = input()

index_snake = 0

for row in range(rows):
    line = deque()
    for col in range(cols):
        if index_snake == len(snake):
            index_snake = 0
        if row % 2 == 0:
            line.append(snake[index_snake])
        else:
            line.appendleft(snake[index_snake])
        index_snake += 1
    print(*line, sep="")





# rows, cols = [int(x) for x in input().split()]
# snake = input()
#
# index_snake = 0
#
# for row in range(rows):
#     line = []
#     for col in range(cols):
#         if index_snake == len(snake):
#             index_snake = 0
#         if row % 2 == 0:
#             line.append(snake[index_snake])
#         else:
#             line.insert(0, snake[index_snake])
#         index_snake += 1
#     print(*line, sep="")