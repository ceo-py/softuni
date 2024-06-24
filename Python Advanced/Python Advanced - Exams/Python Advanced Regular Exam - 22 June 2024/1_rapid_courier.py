from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())
total_weight = 0


while packages and couriers:
    package_weight = packages.pop()
    courier_capacity = couriers.popleft()
    total_weight += min(package_weight, courier_capacity)

    if courier_capacity - package_weight < 0:
        packages.append(package_weight - courier_capacity)

    elif courier_capacity - (2 * package_weight) > 0:
        couriers.append(courier_capacity - (2 * package_weight))


print(f"Total weight: {total_weight} kg")
if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")

elif packages and not couriers:
    print(
        f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages)}")

elif couriers and not packages:
    print(
        f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} but there are no more packages to deliver.")
'''
Input
2 4 6 8
8 6 4 2
'''
