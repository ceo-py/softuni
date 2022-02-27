eggs_size = input()
eggs_color = input()
eggs_number = int(input())

eggs_info = {
    "Large": {
        "Red": 16,
        "Green": 12,
        "Yellow": 9},
    "Medium": {
        "Red": 13,
        "Green": 9,
        "Yellow": 7},
    "Small": {
        "Red": 9,
        "Green": 8,
        "Yellow": 5},
}
total = eggs_info[eggs_size][eggs_color] * eggs_number
total_profit = total - (total * 0.35)
print(f"{total_profit:.2f} leva.")
