fire_levels = input().split("#")
water = int(input())

put_out_cells = list()
effort = 0
total_fire = 0
water_left = water
for clean_text in fire_levels:
    if "High = " in clean_text:
        text = clean_text.replace("High = ", "")

        if int(text) in range(81, 126) and water_left >= int(text):
            put_out_cells.append(text)
            effort += int(text) * 0.25
            total_fire += int(text)
            water_left -= int(text)

    elif "Low = " in clean_text:
        text = clean_text.replace("Low = ", "")

        if int(text) in range(1, 51) and water_left >= int(text):
            put_out_cells.append(int(text))
            effort += int(text) * 0.25
            total_fire += int(text)
            water_left -= int(text)

    elif "Medium = " in clean_text:
        text = clean_text.replace("Medium = ", "")

        if int(text) in range(51, 81) and water_left >= int(text):
            put_out_cells.append(int(text))
            effort += int(text) * 0.25
            total_fire += int(text)
            water_left -= int(text)

print("Cells:")
for n in put_out_cells:
    print(f" - {n}")

print(f"Effort: {effort:.2f}")

print(f"Total Fire: {total_fire}")
