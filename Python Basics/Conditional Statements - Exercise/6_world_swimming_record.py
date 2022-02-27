import math
record = float(input())
distance_meters = float(input())
time_in_sec_per_meter = float(input())

slowing_time_per_fifthen_meter = 12.5
slowing_time_meters = 15
distance_need_to_swim = distance_meters * time_in_sec_per_meter
slowing_time = math.floor(distance_meters / slowing_time_meters) * slowing_time_per_fifthen_meter
# slowing_time = slowing_time * slowing_time_per_fifthen_meter
total_time = distance_need_to_swim + slowing_time

if record > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    total_time = total_time - record
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")