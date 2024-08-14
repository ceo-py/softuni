from collections import deque

bee_groups = deque(int(x) for x in input().split())
bee_eaters_groups = [int(x) for x in input().split()]

while bee_groups and bee_eaters_groups:
    defenders = bee_groups.popleft()
    attackers = bee_eaters_groups.pop()

    attackers_power = attackers * 7

    if defenders == attackers_power:
        continue

    if attackers_power < defenders:
        bee_groups.append(defenders - attackers_power)
        continue

    # base mathod with loop
    # for attack in range(attackers):
    #     defenders -= 7
    #     attackers -= 1
    #
    #     if defenders <= 0:
    #         if defenders < 0:
    #             attackers += 1
    #         break
    #
    # bee_eaters_groups.append(attackers)

    # using pure math no loop
    bee_eaters_groups.append(attackers - (defenders // 7) - (1 if (defenders // 7) * 7 - defenders > 0 else 0))

print("The final battle is over!")

if not bee_groups and not bee_eaters_groups:
    print(f"But no one made it out alive!")
if bee_groups:
    print(f"Bee groups left: {', '.join(str(x) for x in bee_groups)}")
if bee_eaters_groups:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters_groups)}")
