fire_levels = input().split("#")
water = int(input())

put_out_cells = list()
effort = 0
total_fire = 0
water_left = water
for clean_text in fire_levels:
    if "High = " in clean_text:
        text = int(clean_text.replace("High = ", ""))

        if text in range(81, 126) and water_left >= text:
            put_out_cells.append(text)
            effort += text * 0.25
            total_fire += text
            water_left -= text

    elif "Low = " in clean_text:
        text = int(clean_text.replace("Low = ", ""))

        if text in range(1, 51) and water_left >= text:
            put_out_cells.append(text)
            effort += text * 0.25
            total_fire += text
            water_left -= text

    elif "Medium = " in clean_text:
        text = int(clean_text.replace("Medium = ", ""))

        if text in range(51, 81) and water_left >= text:
            put_out_cells.append(int(text))
            effort += text * 0.25
            total_fire += text
            water_left -= text

print("Cells:")
for n in put_out_cells:
    print(f" - {n}")

print(f"Effort: {effort:.2f}")

print(f"Total Fire: {total_fire}")
