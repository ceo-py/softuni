hall_rent = int(input())

figurines = hall_rent * 0.70
catering = figurines * 0.85
sound = catering / 2

total_price = figurines + catering + sound + hall_rent

print(f"{total_price:.2f}")