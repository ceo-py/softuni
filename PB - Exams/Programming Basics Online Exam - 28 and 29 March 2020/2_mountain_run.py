import math

record_in_seconds = float(input())
range_miters = float(input())
claiming_time = float(input())

slowing_time_miters = 50
slowing_time = 30
claiming_miters = range_miters * claiming_time
slowing_per_mitres = math.floor(range_miters / slowing_time_miters)
slowing_per_mitres = slowing_per_mitres * slowing_time
total_time = (claiming_miters + slowing_per_mitres)
total_time_for_record = total_time - record_in_seconds

if record_in_seconds > total_time:
    print(f"Yes! The new record is {total_time:.2f} seconds.")

else:
    print(f"No! He was {total_time_for_record:.2f} seconds slower.")
