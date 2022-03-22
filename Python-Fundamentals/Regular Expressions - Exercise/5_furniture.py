import re
main_string = input()
pattern = re.compile(r">>(\w+)<<(\d+(\.\d+)?)!(\d+)")
names_list = []
total_price = 0

while main_string != "Purchase":
    matches = pattern.finditer(main_string)
    for show in matches:
        names_list.append(show[1])
        total_price += (float(show[2]) * int(show[4]))
    main_string = input()

print("Bought furniture:")
if names_list:
    for name in names_list:
        print(name)
print(f"Total money spend: {total_price:.2f}")


