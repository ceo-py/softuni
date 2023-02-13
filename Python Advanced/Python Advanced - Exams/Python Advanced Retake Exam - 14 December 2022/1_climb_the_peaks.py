from collections import deque

daily_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks, mountain_peaks = [], [{"Vihren": 80}, {"Kutelo": 90}, {"Banski Suhodol": 100}, {"Polezhan": 60}, {"Kamenitza": 70}]

while daily_portions and daily_stamina and mountain_peaks:
    boost_sum = daily_portions.pop() + daily_stamina.popleft()
    peak_name, difficult_level = list(mountain_peaks[0].items())[0]

    if boost_sum >= difficult_level:
        del mountain_peaks[0]
        conquered_peaks.append(peak_name)

if not mountain_peaks:
    result_conquered = "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"

else:
    result_conquered = "Alex failed! He has to organize his journey better next time -> @PIRINWINS"

print(result_conquered)
if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
