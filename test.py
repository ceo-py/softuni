import math
x_area_sqm = int(input())
y_greap_sqm = float(input())
z_necessery_vine = int(input())
workers = int(input())
kolichestvo = (x_area_sqm*0.4*y_greap_sqm/2.5)
if kolichestvo < z_necessery_vine:
    q = (z_necessery_vine - kolichestvo)
    print(f'It will be a tough winter! More {math.floor(q)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(kolichestvo)} liters.')
    v = (kolichestvo - z_necessery_vine)/workers
    vino_poveche = (kolichestvo-z_necessery_vine)
    print(f'{math.ceil(vino_poveche)} liters left -> {math.ceil(v)} liters per person.')