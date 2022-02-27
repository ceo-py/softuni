stadium_capacity = int(input())
number_fans = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for _ in range(1, number_fans + 1):
    sector_type = input()

    if sector_type == "A":
        a_sector += + 1

    elif sector_type == "B":
        b_sector += + 1

    elif sector_type == "V":
        v_sector += + 1

    elif sector_type == "G":
        g_sector += + 1

a_sector = (a_sector / number_fans) * 100
b_sector = (b_sector / number_fans) * 100
v_sector = (v_sector / number_fans) * 100
g_sector = (g_sector / number_fans) * 100
total_fans_on_stadium = (number_fans / stadium_capacity) * 100

print(f"{a_sector:.2f}%\n{b_sector:.2f}%\n{v_sector:.2f}%\n{g_sector:.2f}%\n{total_fans_on_stadium:.2f}%")
