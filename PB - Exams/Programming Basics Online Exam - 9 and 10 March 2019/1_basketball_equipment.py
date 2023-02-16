yearly_tax = int(input())

basketball_sneakers = yearly_tax * 0.60
basketball_equip = basketball_sneakers * 0.80
basketball_ball = basketball_equip / 4
basketball_accessories = basketball_ball / 5

total_sum_needed = yearly_tax + basketball_accessories + basketball_equip + basketball_ball + basketball_sneakers

print(f"{total_sum_needed:.2f}")
