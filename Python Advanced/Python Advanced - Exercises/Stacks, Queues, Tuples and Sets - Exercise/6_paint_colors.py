month = input()
nights = int(input())
ap = 0
stu = 0
if 0 < nights <= 7:
    if month == 'May' or month == 'October':
        ap = 65*nights
        stu = 50*nights
    if month == 'June' or month == 'September':
        ap = 68.7*nights
        stu = 75.2*nights
    if month == 'July' or month == 'August':
        ap = 77*nights
        stu = 76*nights
if 7 < nights <= 14:
    if month == 'May' or month == 'October':
        ap = 65*nights
        stu = 50*nights*0.95
    if month == 'June' or month == 'September':
        ap = 68.7*nights
        stu = 75.2*nights
    if month == 'July' or month == 'August':
        ap = 77*nights
        stu = 76*nights
if nights > 14:
    if month == 'May' or month == 'October':
        ap = 65*nights*0.9
        stu = 50*nights*0.7
    if month == 'June' or month == 'September':
        ap = 68.7*nights
        stu = 75.2*nights*0.8
    if month == 'July' or month == 'August':
        ap = 77*nights*0.9
        stu = 76*nights
print(f'Apartment: {ap:.2f} lv.')
print(f'Studio: {stu:.2f} lv.')
