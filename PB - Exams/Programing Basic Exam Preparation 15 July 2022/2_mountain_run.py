record_in_seconds = float(input())
distance_meters = float(input())
time_for_one_meter = float(input())

claiming_time = distance_meters * time_for_one_meter
slowing_time = int(distance_meters / 50) * 30
total_time = claiming_time + slowing_time

if total_time < record_in_seconds:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    diffrence = abs(total_time - record_in_seconds)
    print(f"No! He was {diffrence:.2f} seconds slower.")

