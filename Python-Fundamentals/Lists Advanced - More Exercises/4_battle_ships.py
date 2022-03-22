rows_on_field = int(input())

battle_field_list = []
ship_destroyed = 0


def battle_field(rows):
    for _ in range(rows):
        battle_field_list.append([int(n) for n in input().split()])


def attack_ships(positions):
    global ship_destroyed
    for attack in positions:
        attack = attack.split("-")
        row_attack = int(attack[0])
        col_attack = int(attack[-1])
        for target_row, target_index in enumerate(battle_field_list):
            if target_row == row_attack:
                if target_index[col_attack] >= 1:
                    target_index[col_attack] -= 1
                    if target_index[col_attack] == 0:
                        ship_destroyed += 1
                break


battle_field(rows_on_field)
attacks = input().split()
attack_ships(attacks)
print(ship_destroyed)
