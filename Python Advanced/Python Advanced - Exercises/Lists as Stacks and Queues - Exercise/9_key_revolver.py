from collections import deque

bullet_price = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence = int(input())

barrel_count, shoot_count = 0, 0

while bullets and locks:
    barrel_count += 1
    shoot_count += 1
    bullet = bullets.pop()
    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if barrel_count == size_of_the_gun_barrel and bullets:
        print("Reloading!")
        barrel_count = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs((shoot_count * bullet_price) - intelligence)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")