town_name = input()
extras = input()
vip_packet = input()
days_to_stay = int(input())

towns = ["Varna", "Burgas", "Bansko", "Borovets"]
packets_type = ["withEquipment", "noEquipment", "withBreakfast", "noBreakfast"]
total = 0

if town_name not in towns or extras not in packets_type:
    print(f"Invalid input!")

elif days_to_stay < 1:
    print(f"Days must be positive number!")

else:
    if days_to_stay > 7:
        days_to_stay = days_to_stay - 1

    if ("Bansko" == town_name or "Borovets" == town_name) and extras == "withEquipment" and vip_packet == "yes":
        total = (days_to_stay * 100) - ((days_to_stay * 100) * 0.10)

    elif ("Bansko" == town_name or "Borovets" == town_name) and extras == "noEquipment" and vip_packet == "yes":
        total = (days_to_stay * 80) - ((days_to_stay * 80) * 0.05)

    elif ("Bansko" == town_name or "Borovets" == town_name) and extras == "noEquipment" and vip_packet == "no":
        total = (days_to_stay * 80)

    elif ("Bansko" == town_name or "Borovets" == town_name) and extras == "withEquipment" and vip_packet == "no":
        total = (days_to_stay * 100)

    elif ("Varna" == town_name or "Burgas" == town_name) and extras == "withBreakfast" and vip_packet == "yes":
        total = (days_to_stay * 130) - ((days_to_stay * 130) * 0.12)

    elif ("Varna" == town_name or "Burgas" == town_name) and extras == "noBreakfast" and vip_packet == "yes":
        total = (days_to_stay * 100) - ((days_to_stay * 100) * 0.07)

    elif ("Varna" == town_name or "Burgas" == town_name) and extras == "noBreakfast" and vip_packet == "no":
        total = (days_to_stay * 100)

    elif ("Varna" == town_name or "Burgas" == town_name) and extras == "withBreakfast" and vip_packet == "no":
        total = (days_to_stay * 130)

    print(f"The price is {total:.2f}lv! Have a nice time!")
