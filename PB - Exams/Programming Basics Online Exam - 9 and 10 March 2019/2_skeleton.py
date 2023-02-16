minutes_control = int(input())
seconds_control = int(input())
length_chute = float(input())
seconds_per_100_meters = int(input())

control_time = minutes_control * 60 + seconds_control
slowing_time = length_chute / 120
total_slowing_time = slowing_time * 2.5
marin_time = (length_chute / 100) * seconds_per_100_meters - total_slowing_time

if marin_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {marin_time - control_time:.3f} second slower.")