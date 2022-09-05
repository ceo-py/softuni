from collections import deque

eggs_size = deque(int(x) for x in input().split(", "))
paper_size = [int(x) for x in input().split(", ")]
BOXES_SIZE = 50
filled_boxes = 0

while eggs_size and paper_size:
    egg = eggs_size.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue
    paper = paper_size.pop()
    wrapping_size = egg + paper
    if wrapping_size <= BOXES_SIZE:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")

if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")
