minutes_controla = int(input())
secondes_controla = int(input())
length_hive_meters = float(input())
seconds_for_sto_meters = int(input())

time_controla = minutes_controla * 60 + secondes_controla
time_decrease = length_hive_meters / 120
total_decrease_time = time_decrease * 2.5
martin_time = (length_hive_meters / 100) * seconds_for_sto_meters - total_decrease_time
control_time = martin_time - time_controla

if martin_time <= time_controla:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {martin_time:.3f}.")

else:
    print(f"No, Marin failed! He was {control_time:.3f} second slower.")
