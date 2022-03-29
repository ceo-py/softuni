wins, losses, draw = 0, 0, 0
 
for _ in range(3):
    home_team, away_team = input().split(":")
    if home_team > away_team:
        wins += 1
    elif home_team == away_team:
        draw += 1
    else:
        losses += 1
 
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draw}")
