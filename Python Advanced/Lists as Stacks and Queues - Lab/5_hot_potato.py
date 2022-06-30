from collections import deque

kids = deque(input().split())
number_of_skips = int(input())

while len(kids) > 1:
    kids.rotate(-number_of_skips)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.popleft()}")
