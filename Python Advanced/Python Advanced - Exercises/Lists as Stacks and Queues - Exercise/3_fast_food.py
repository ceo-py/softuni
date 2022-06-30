from collections import deque

quantity_of_the_food = int(input())
orders = deque(int(x) for x in input().split())


print(max(orders))
while orders:
    order_number = orders.popleft()
    if quantity_of_the_food - order_number >= 0:
        quantity_of_the_food -= order_number
    else:
        print(f"Orders left: {order_number}", *orders)
        break
else:
    print("Orders complete")

