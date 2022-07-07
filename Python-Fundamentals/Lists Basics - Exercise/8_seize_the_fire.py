fire_levels = input().split("#")
water = int(input())

put_out_cells = list()
effort, total_fire, water_left = 0, 0, water

for clean_text in fire_levels:
    type_of_fire, cell_value = [int(x) if x.isdigit() else x for x in clean_text.split(" = ")]
    if water_left >= cell_value:
        if any(["High" in type_of_fire and cell_value in range(81, 126),
                "Low" in type_of_fire and cell_value in range(1, 51),
                "Medium" in type_of_fire and cell_value in range(51, 81)]):
            put_out_cells.append(cell_value)
            effort += cell_value * 0.25
            total_fire += cell_value
            water_left -= cell_value

print("Cells:")
for n in put_out_cells:
    print(f" - {n}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
