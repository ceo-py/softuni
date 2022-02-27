t_shirt_price = float(input())
target_money = float(input())

shorty = t_shirt_price * 0.75
socks = shorty * 0.20
shoes = (shorty + t_shirt_price) * 2
off = 0.15

total = shorty + shoes + socks + t_shirt_price
total_with_off = total - total * off
diffrence = abs(total_with_off - target_money)

if total_with_off >= target_money:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_with_off:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diffrence:.2f} lv. more.")
