from collections import deque

kids = deque(input().split())
number_of_skips = int(input())

while len(kids) > 1:
    kids.rotate(-number_of_skips)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.popleft()}")




# from collections import deque
# kids = deque(input().split())
# tosses = int(input())
#
# while len(kids) > 1:
#     for num in range(1, tosses + 1):
#         if num % tosses == 0:
#             print(f"Removed {kids.popleft()}")
#             break
#         kids.append(kids.popleft())
#
# print(f"Last is {kids.pop()}")