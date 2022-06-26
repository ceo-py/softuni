needed_xp = float(input())
count_battles = int(input())


total_xp = 0
battles_num = 0
for battle in range(1, count_battles + 1):
    xp_per_battle = float(input())
    if battle % 3 == 0:
        xp_per_battle *= 1.15
    if battle % 5 == 0:
        xp_per_battle *= 0.90
    if battle % 15 == 0:
        xp_per_battle *= 1.05
    total_xp += xp_per_battle
    battles_num = battle
    if total_xp >= needed_xp:
        break

if total_xp >= needed_xp:
    print(f"Player successfully collected his needed experience for {battles_num} battles.")
else:
    missing_xp = abs(total_xp - needed_xp)
    print(f"Player was not able to collect the needed experience, {missing_xp:.2f} more needed.")







